import uuid
from django.http import response

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase

from the_eye.models import Event


class EventViewSetTests(APITransactionTestCase):
    """Test suite for testing Event API"""

    def test_create_event(self):
        """Ensures Event Creation"""

        url = reverse("event-list")
        body = {
            "session_id": "10e9932e-3c7e-4716-bb69-c8005d1b9661",
            "category": "page interaction",
            "name": "pageview",
            "data": {"host": "www.ahost.com", "path": "/"},
            "timestamp": "2021-07-27 04:43:10.243860",
        }

        response = self.client.post(url, body, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(
            Event.objects.get().session_id,
            uuid.UUID("10e9932e-3c7e-4716-bb69-c8005d1b9661"),
        )
