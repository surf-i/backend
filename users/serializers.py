from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    calificacion = serializers.FloatField(min_value=0, max_value=5)
    gradoVeracidad = serializers.FloatField(min_value=0, max_value=99)
    calificacionDisenoPromedio = serializers.FloatField(min_value=0, max_value=99, allow_null=True)
    calificacionUsabilidadPromedio = serializers.FloatField(min_value=0, max_value=99, allow_null=True)
    
    class Meta:
        model = Review
        fields = '__all__'