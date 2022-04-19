from django.db import models
from websites.models import Website, Categoria
from store.models import Funcionalidad
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import uuid
# Create your models here.


class TipoUsuario(models.Model):
    class TipoUsuarioEnum(models.TextChoices):
        FREE = 'FREE', _('Free')
        SURFIER = 'SURFIER', _('Surfier')
    tipo = models.CharField(null=False, max_length=50, choices=TipoUsuarioEnum.choices, default=TipoUsuarioEnum.FREE, primary_key=True)

    def is_upperclass(self):
        return self.tipo in {
            self.TipoUsuarioEnum.FREE,
            self.TipoUsuarioEnum.SURFIER,
        }
    
    def __str__(self):
        return f"{self.tipo}"

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, models.CASCADE, unique=True, default="")
    nombre = models.CharField(max_length=100, null=False)
    puntos = models.IntegerField(null=False, default=0)
    fechaVencimiento = models.DateField(null=False)
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ('tipoUsuario', 'user')
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['user'], name='unique_user')]

    def __str__(self):
        return f"Usuario: {self.user.username}"

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comentario = models.CharField(max_length=254)
    calificacion = models.DecimalField(null=False, decimal_places=2, max_digits=4)
    fecha = models.DateTimeField(null=False)
    gradoVeracidad = models.DecimalField(null=True, decimal_places=2, max_digits=4)
    website = models.ForeignKey(Website, null=False, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, null=False, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Review de Usuario: {self.usuario}, Website: {self.website}"