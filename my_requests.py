import requests
import json

# Define the API endpoint URL
url = 'http://127.0.0.1:5000/recommend'

# Define the user input data
user_input = {
    'AGE': 25,
    'Interest': 'Di Tích Lịch Sử, Món ăn ngon',
    'Bạn đi với': 'Gia đình',
    'Visiting time': '2 ngày 1 đêm',
    'sex': 'Nam',
    'Desired amount': 'Từ 1 đến 3 triệu'
}

# Send a POST request to the API with the user input data
response = requests.post(url, json=user_input)

# Get the JSON response
output = response.json()

# Print the recommended places
print(output['top_recommended_places'])