from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

class AccountTests(APITestCase):
    def test_send_json_request1(self):
        data = {'key': '1.1.1.1.1.1.1', 'items': 3, 'mandates': [1, 2, 3], 'preferences': [[1, 2, 3], [2, 1, 3], [3, 2, 1]]}
        response = self.client.post("https://faircol.herokuapp.com/api/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, -1)
        
    def test_send_wrong_json_request(self):
        data = {'key': '1.1.1.1.1.1.1', 'items': 3, 'mandates': [1, 2, 3], 'preferences': [[2, 1, 3], [3, 2, 1]]}
        response = self.client.post("https://faircol.herokuapp.com/api/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, -1)

    def test_send_not_json_request(self):
        data = "not json"
        response = self.client.post("https://faircol.herokuapp.com/api/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, -1)

    def test_retrieving_session(self):
        data = {'key': '3.3.3.3.3.3.3', 'items': 3, 'mandates': [1, 2, 3], 'preferences': [[1, 2, 3], [2, 1, 3], [3, 2, 1]]}
        respone = self.client.post("https://faircol.herokuapp.com/api/", data, format='json')
        self.assertEqual(respone.status_code, status.HTTP_200_OK)
        data = {'key': '3.3.3.3.3.3.3'}
        respone = self.client.post("https://faircol.herokuapp.com/api/getsave", data, format='json')
        self.assertEqual(respone.status_code, status.HTTP_200_OK)
        self.assertEqual(respone.data, "[[1, 2, 3], [2, 1, 3], [3, 2, 1]]")
        
    def test_retrieving_nonexisting_session(self):
        data = {'key': 'Not.a.key.at.all'}
        respone = self.client.post("https://faircol.herokuapp.com/api/getsave", data, format='json')
        self.assertEqual(respone.status_code, status.HTTP_200_OK)
        self.assertEqual(respone.data, -1)
    
    def test_retrieving_not_a_json_key_session(self):
        data = "not json"
        respone = self.client.post("https://faircol.herokuapp.com/api/getsave", data, format='json')
        self.assertEqual(respone.status_code, status.HTTP_200_OK)
        self.assertEqual(respone.data, -1)
        