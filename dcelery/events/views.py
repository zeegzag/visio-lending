import logging
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer

logger = logging.getLogger('events')

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date', 'location']
    ordering_fields = ['date']

    def perform_create(self, serializer):
        event = serializer.save()
        # Log the creation of the event
        logger.info(f"New Event Created: {event.title} at {event.location} on {event.date}")

    def perform_update(self, serializer):
        event = serializer.save()
        # Log the update of the event
        logger.info(f"Event Updated: {event.title} at {event.location} on {event.date}")
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Log the deletion of the event
        logger.info(f"Event Deleted: {instance.title} at {instance.location} on {instance.date}")
        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Log the retrieval of a single event
        logger.info(f"Event Retrieved: {instance.title} at {instance.location} on {instance.date}")
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        # Log the list retrieval of all events
        logger.info("Event List Retrieved")
        return super().list(request, *args, **kwargs)
