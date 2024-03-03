from rest_framework import serializers
from .models import TrashPost

class TrashPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashPost
        fields = ('author', 'image', 'location', 'created_at')