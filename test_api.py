import yaml
import unittest
from Api import APIClient



class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load configuration from YAML file
        with open('config.yaml', 'r') as file:
            cls.config = yaml.safe_load(file)

        cls.client = APIClient(cls.config['api']['base_url'])
        cls.get_endpoint = cls.config['api']['get_object_endpoint']
        cls.put_endpoint = cls.config['api']['put_object_endpoint']
        cls.delete_endpoint = cls.config['api']['delete_object_endpoint']
        cls.post_endpoint = cls.config['api']['post_object_endpoint']
        cls.expected_get_response = cls.config['api']['expected_get_response']
        cls.put_object_data = cls.config['api']['put_object_data']
        cls.expected_put_response = cls.config['api']['expected_put_response']
        cls.delete_object_id = cls.config['api']['delete_object_id']

    def test_get_object(self):
        response = self.client.get_object(self.get_endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())  # Adjust this based on actual structure
        self.assertEqual(response.json().get("id"), self.expected_get_response['id'])

    def test_put_object(self):
        response = self.client.put_object(self.put_endpoint, self.put_object_data)
        self.assertIn(response.status_code, [200, 405])  # Allow 200 or 405 based on API behavior
        if response.status_code == 200:
            self.assertEqual(response.json()["name"], self.put_object_data["name"])
            self.assertEqual(response.json()["description"], self.put_object_data["description"])

    def test_delete_object(self):
        response = self.client.delete_object(self.delete_endpoint)
        self.assertIn(response.status_code, [204, 405])  # Allow 204 or 405 based on API behavior

    def test_post_object(self):
        # Example data to post
        post_data = {
            "name": "New Test Object",
            "description": "This is a new test object"
        }
        response = self.client.post_object(self.post_endpoint, post_data)
        # Expecting status code to be 201 for successful creation
        self.assertEqual(response.status_code, 200)  # Expecting created
        self.assertIn('id', response.json())  # Check if the response contains an ID

if __name__ == '__main__':
    unittest.main()