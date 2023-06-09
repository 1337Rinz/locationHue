# locationHue
# Recommendation API

This API provides recommendations for places to visit based on user input. It uses a dataset of places in Huế city and uses cosine similarity to generate recommendations.

## Getting Started

To get started with the API, follow the instructions below.

### Prerequisites

- Python 3.x
- Flask
- Pandas
- scikit-learn

### Installation

1. Clone the repository:
git clone https://github.com/1337Rinz/locationHue.git


2. Install the required dependencies:
pip install flask pandas scikit-learn

3. Run the API:

The API will be accessible at http://localhost:5000.

## API Endpoints

### POST /recommend

This endpoint accepts a JSON payload containing user input and returns a JSON response with recommended places to visit.

Example Request:

POST /recommend
Content-Type: application/json

{
"AGE": 25,
"Interest": "Di Tích Lịch Sử, Món ăn ngon",
"Bạn đi với": "Gia đình",
"Visiting time": "2 ngày 1 đêm",
"sex": "Nam",
"Desired amount": "Từ 1 đến 3 triệu"
}
Example Response:

HTTP/1.1 200 OK
Content-Type: application/json

{
"top_recommended_places": [
"Cố đô Huế",
"Đồi Vọng Cảnh",
"Chùa Thiên Mụ",
"Vườn hoa Bách Vân",
"Chợ Đông Ba"
]
}

### GET /recommend

This endpoint provides a welcome message to verify that the API is running.

Example Request:
GET /recommend

Example Response:
HTTP/1.1 200 OK
Content-Type: application/json

{
"message": "Welcome to the recommendation API"
}


## Notes

- The dataset used for recommendations is sourced from [[link](https://raw.githubusercontent.com/1337Rinz/DATA_for_machine_learning/main/dataHUE.csv)].
- The API provides recommendations based on cosine similarity between user input and the available places in the dataset.

Feel free to customize the API endpoints, response messages, and dataset as per your needs.

