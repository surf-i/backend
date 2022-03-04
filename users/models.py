from django.db import models
from websites.models import Website, Categoria
from store.models import Funcionalidad
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.


class TipoUsuario(models.Model):
    class TipoUsuarioEnum(models.TextChoices):
        FREE = 'FREE', _('Free')
        SURFIER = 'SURFIER', _('Surfier')
        ADMIN = 'ADMIN', _('Admin')
    tipo = models.CharField(null=False, max_length=50, choices=TipoUsuarioEnum.choices, default=TipoUsuarioEnum.FREE, primary_key=True)

    def is_upperclass(self):
        return self.tipo in {
            self.TipoUsuarioEnum.FREE,
            self.TipoUsuarioEnum.SURFIER,
            self.TipoUsuarioEnum.ADMIN
        }
    
    def __str__(self):
        return f"{self.tipo}"

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    correo = models.EmailField(max_length=254, null=False, unique=True)
    contrasena = models.CharField(max_length=254, null=False)
    nombre = models.CharField(max_length=100, null=False)
    puntos = models.IntegerField(null=False, default=0)
    fechaVencimiento = models.DateField(null=False)
    tipoUsuario = models.ForeignKey(TipoUsuario, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.correo}"

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comentario = models.CharField(max_length=254)
    calificacion = models.DecimalField(null=False, decimal_places=2, max_digits=4)
    fecha = models.DateTimeField(null=False)
    gradoVeracidad = models.DecimalField(null=True, decimal_places=2, max_digits=4)
    website = models.ForeignKey(Website, null=False, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, null=False, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE)
    funcionalidadesDesbloqueadas = models.ManyToManyField(Funcionalidad, default=None)
    

    def __str__(self):
        return f"Review de Usuario: {self.usuario}, Website: {self.website}"