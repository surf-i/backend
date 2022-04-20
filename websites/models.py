from enum import unique
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

class Categoria(models.Model):
    class CategoriaEnum(models.TextChoices):
        SOCIAL = 'SOCIAL', _('Social')
        ENTRETENIMIENTO = 'ENTRETENIMIENTO', _('Entretenimiento')
        NOTICIAS = 'NOTICIAS',_('Noticias')
        ACADEMICO = 'ACADEMICO', _('Academico')
        OPINION = 'OPINION', _('Opinion')
        COMERCIO = 'COMERCIO', _('Comercio')
        TECNOLOGIA = 'TECNOLOGIA', _('Tecnologia')
        PRODUCTIVIDAD = 'PRODUCTIVIDAD', _('Productividad')
        TURISMO = 'TURISMO', _('Turismo')
        INVESTIGACION = 'INVESTIGACION', _('Investigacion')
        PERIODISMO = 'PERIODISMO', _('Periodismo')
    tipo = models.CharField(null=False, max_length=50, choices=CategoriaEnum.choices, default=CategoriaEnum.SOCIAL, primary_key=True)

    def is_upperclass(self):
        return self.tipo in {
            self.CategoriaEnum.SOCIAL,
            self.CategoriaEnum.ENTRETENIMIENTO,
            self.CategoriaEnum.NOTICIAS,
            self.CategoriaEnum.ACADEMICO,
            self.CategoriaEnum.OPINION,
            self.CategoriaEnum.COMERCIO,
            self.CategoriaEnum.TECNOLOGIA,
            self.CategoriaEnum.PRODUCTIVIDAD,
            self.CategoriaEnum.TURISMO,
            self.CategoriaEnum.INVESTIGACION,
            self.CategoriaEnum.PERIODISMO
        }

    def __str__(self):
        return f"{self.tipo}"
        

class Website(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(null=False, max_length=50)
    url = models.URLField(null=False, max_length=50)
    calificacionPromedio = models.DecimalField(null=False, decimal_places=2, max_digits=4)
    gradoVeracidadPromedio = models.DecimalField(null=False, decimal_places=2, max_digits=4)
    categorias = models.ManyToManyField(Categoria, default=None)

    def __str__(self):
        return f"{self.nombre}"   

class ReviewMetadata(models.Model):
    website = models.OneToOneField(Website, on_delete=models.CASCADE, primary_key=True)
    numReviews = models.IntegerField(null=False, default=0)
    sumaCalificacion = models.IntegerField(null=False, default=0)
    sumaVeracidad = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f"Review Metadata de: {self.website}"

class DatosCategoria(models.Model):
    website = models.OneToOneField(Website, null=False, primary_key=True, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Categoria, null=False, on_delete=models.CASCADE)
    cantReviews = models.IntegerField(null=False, default=0)

    class Meta:
        unique_together = ('website', 'tipo')

    def __str__(self):
        return f"Datos de Website: {self.website}"
