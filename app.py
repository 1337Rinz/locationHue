from flask import Flask, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/1337Rinz/DATA_for_machine_learning/main/dataHUE.csv', delimiter=';')

# Data preprocessing
df = df.fillna('')
df_encoded = pd.get_dummies(df.drop(columns=['địa điểm tham quan']))
similarity_matrix = cosine_similarity(df_encoded.T)


@app.route('/recommend', methods=['GET', 'POST'])
def recommend_places():
    if request.method == 'POST':
        # Get user input from the request
        user_input = request.json

        if user_input is None:
            return jsonify({'error': 'Invalid input data'}), 400

        # Create a DataFrame for the user input
        user_df = pd.DataFrame(user_input, index=[0])

        # Encode the user's input
        user_encoded = pd.get_dummies(user_df)

        # Recommend places to visit for the user
        similar_items_indices = similarity_matrix[user_encoded.values.argmax()].argsort()[::-1]
        recommended_places = []
        for idx in similar_items_indices:
            places = df['địa điểm tham quan'].iloc[idx].split(', ')
            for place in places:
                if place not in recommended_places:
                    recommended_places.append(place)
                    if len(recommended_places) >= 5:
                        break
            if len(recommended_places) >= 5:
                break

        # Convert the recommendations to JSON format
        output = {'top_recommended_places': recommended_places}

        # Return the JSON response
        return jsonify(output), 200
    else:
        return jsonify({'message': 'Welcome to the recommendation API'}), 200


if __name__ == '__main__':
    app.run()
