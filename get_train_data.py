import requests


def get_details():
    url = "http://20.244.56.144/train/trains"
    access_token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTAwNDc2MzMsImNvbXBhbnlOYW1lIjoiVHJhaW4gQ2VudHJhbCIsImNsaWVudElEIjoiYmMxNDFmMDktMjYwNS00OTk2LWFlYTYtYzgzNzY0N2Y3ZGFhIiwib3duZXJOYW1lIjoiIiwib3duZXJFbWFpbCI6IiIsInJvbGxObyI6IjIwMDEwMTIzNCJ9.huHQPuruU4XpHFdeW8IWYErdNkWQu7wSobVyAZAnnMY"
    query_params = [
        {
            "trainName": "Chennai Exp",
            "trainNumber": "2344", 
            "departureTime": {
                "Hours": 21, 
                "Minutes": 35,
                "Seconds": 0
            },
            "seatsAvailable": { 
                "sleeper": 3,
                "AC": 1
            },
            "price": { 
                "sleeper": 2,
                "AC": 5
            },
            "delayedBy": 15
        },
        {
            "trainName": "Hyderabad Exp", 
            "trainNumber": "2341",
            "departureTime": {
                "Hours": 23,
                "Minutes": 55,
                "Seconds": 0
            },
            "seatsAvailable": {
                "sleeper": 6, 
                "AC": 7
            },
            "price": {
                "sleeper": 554, 
                "AC": 1854
            },
            "delayedBy": 5
        }
    ]

    try:
        response = requests.get(url, headers={'Authorization': 'token {}'.format(access_token)})
        response_data = response.json()

        if response.status_code == 200:
            return response_data
        else:
            print("Failed to fetch event details.")
            print("Error message:", response_data.get("error"))
            return []

    except requests.exceptions.RequestException as e:
        print("Error occurred while making the API request:", e)
        return []
