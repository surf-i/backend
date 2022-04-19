from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
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