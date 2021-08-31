import uuid
from django.test import TransactionTestCase
from the_eye.models import Event


class EventModelTestCase(TransactionTestCase):
    """Defines the test suite for Event model."""

    def test_can_create_event_model(self):
        """Tests the event model creation"""

        self.event = Event(
            session_id=uuid.uuid4(),
            category="page interaction",
            name="pageview",
            data={"host": "www.ahost.com", "path": "/"},
            timestamp="2021-07-27 04:43:10.243860",
        )

        old_count = Event.objects.count()

        self.event.save()
        new_count = Event.objects.count()

        self.assertEqual(old_count + 1, new_count)
