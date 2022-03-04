from django.db import models
import uuid
# Create your models here.

class Funcionalidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(null=False, max_length=50)
    precio = models.IntegerField(null=False, default=0)
    descripcion = models.CharField(null=False, max_length=254)
    tipo = models.CharField(null=False, max_length=254)