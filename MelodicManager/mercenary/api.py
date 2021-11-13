from rest_framework.decorators import permission_classes
from .models import Track
from rest_framework import viewsets, permissions
from .serializers import TrackSerializer

#Track Viewset
class TrackViewSet(viewsets.ModelViewSet):
     queryset =Track.objects.all()
     permission_classes = [
         permissions.AllowAny
     ]
     serializer_class = TrackSerializer