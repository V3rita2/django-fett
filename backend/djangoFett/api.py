from .models import Track
from rest_framework import viewsets, permissions
from .serializers import TrackSerializer

# Track viewset

class TrackViewset(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TrackSerializer