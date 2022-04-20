from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    calificacion = serializers.FloatField(min_value=0, max_value=5)
    gradoVeracidad = serializers.FloatField(min_value=0, max_value=99)
    class Meta:
        model = Review
        fields = ('id', 
                'comentario', 
                'calificacion', 
                'fecha', 
                'gradoVeracidad', 
                'website', 
                'categoria', 
                'usuario')