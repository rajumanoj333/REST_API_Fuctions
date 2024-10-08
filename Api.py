import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_object(self, endpoint):
        response = requests.get(f"{self.base_url}{endpoint}")
        return response

    def put_object(self, endpoint, data):
        response = requests.put(f"{self.base_url}{endpoint}", json=data)
        return response

    def delete_object(self, endpoint):
        response = requests.delete(f"{self.base_url}{endpoint}")
        return response

    def post_object(self, endpoint, data):
        response = requests.post(f"{self.base_url}{endpoint}", json=data)
        return response

# Example usage for the above function
if __name__ == "__main__":
    client = APIClient("https://api.restful-api.dev")#base url
    response = client.get_object("/objects/ff808181923ed5e2019251c44f38283d")#adding endpoint
    print("GET Response:", response.json())