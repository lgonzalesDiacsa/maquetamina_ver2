from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from restapp.models import PostCardIDEvent

class restappSerializer(ModelSerializer):
    h_evento = serializers.TimeField(format='%H:%M:%S') 
    class Meta:
        model = PostCardIDEvent
        fields = ['id', 'cardid', 'f_evento', 'h_evento', 'evento']
        