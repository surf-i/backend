from rest_framework import serializers
from .models import Website


class WebsiteSerializer(serializers.ModelSerializer):
    autor = serializers.CharField(allow_null=True)
    fecha = serializers.DateField(allow_null=True)
    
    class Meta:
        model = Website
        fields = '__all__'
