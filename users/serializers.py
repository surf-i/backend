from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    calificacion = serializers.FloatField(min_value=0, max_value=5)
    gradoVeracidad = serializers.FloatField(min_value=0, max_value=99)
    calificacionDiseno = serializers.FloatField(min_value=0, max_value=99, allow_null=True)
    calificacionUsabilidad = serializers.FloatField(min_value=0, max_value=99, allow_null=True)

    class Meta:
        model = Review
        fields = '__all__'