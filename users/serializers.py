from rest_framework import serializers
from .models import Review
from dj_rest_auth.registration.serializers import RegisterSerializer


class ReviewSerializer(serializers.ModelSerializer):
    comentario = serializers.CharField(allow_null=True)
    calificacion = serializers.FloatField(min_value=0, max_value=5)
    gradoVeracidad = serializers.FloatField(min_value=0, max_value=99)
    calificacionDiseno = serializers.FloatField(min_value=0, max_value=99, allow_null=True)
    calificacionUsabilidad = serializers.FloatField(min_value=0, max_value=99, allow_null=True)

    class Meta:
        model = Review
        fields = '__all__'

class SurfiRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }