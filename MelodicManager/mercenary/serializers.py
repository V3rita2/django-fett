from django.db.models import fields
from rest_framework import serializers
from .models import Track

#track serializer

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'