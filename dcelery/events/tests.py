from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Event

class EventAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.event_data = {
            "title": "Meeting",
            "description": "Team meeting",
            "date": "2024-12-15T10:00:00Z",
            "location": "Board Room"
        }
        self.event = Event.objects.create(**self.event_data)

    def test_create_event(self):
        response = self.client.post('/api/events/', self.event_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_event(self):
        response = self.client.get(f'/api/events/{self.event.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_event(self):
        updated_data = {"title": "Updated Meeting"}
        response = self.client.patch(f'/api/events/{self.event.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Meeting")

    def test_delete_event(self):
        response = self.client.delete(f'/api/events/{self.event.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
