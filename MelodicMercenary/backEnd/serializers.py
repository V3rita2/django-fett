from rest_framework import serializers
from .models import Track


class TrackSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Track
        fields = ('title', 'image', 'created_at')
#REMEMBER TO UPDATE ANY VIEWS USING THIS