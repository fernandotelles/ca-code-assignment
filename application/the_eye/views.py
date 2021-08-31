from django.shortcuts import render

from rest_framework import viewsets
from the_eye.models import Event
from the_eye.serializers import EventSerializer

# Create your views here.


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.select_for_update().all().order_by("-timestamp")
    serializer_class = EventSerializer
