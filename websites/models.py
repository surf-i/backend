from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

class Categoria(models.Model):
    class CategoriaEnum(models.TextChoices):
        NOT_RATED = 'NOT RATED', _('Not Rated')
        SOCIAL = 'SOCIAL', _('Social')
        ENTERTAINMENT = 'ENTERTAINMENT', _('Entertainment')
        BUSINESS_ORG = 'BUSINESS/ORG',_('Business/Org')
        ACADEMIC = 'ACADEMIC', _('Academic')
        SHOPPING = 'SHOPPING', _('Shopping')
        TECHNOLOGY = 'TECHNOLOGY', _('Technology')
        PRODUCTIVITY = 'PRODUCTIVITY', _('Productivity')
        RESEARCH = 'RESEARCH', _('Research')
        NEWS = 'NEWS', _('News')
    tipo = models.CharField(null=False, max_length=50, choices=CategoriaEnum.choices, default=CategoriaEnum.NOT_RATED, primary_key=True)

    def is_upperclass(self):
        return self.tipo in {
            self.CategoriaEnum.NOT_RATED,
            self.CategoriaEnum.SOCIAL,
            self.CategoriaEnum.ENTERTAINMENT,
            self.CategoriaEnum.BUSINESS_ORG,
            self.CategoriaEnum.ACADEMIC,
            self.CategoriaEnum.SHOPPING,
            self.CategoriaEnum.TECHNOLOGY,
            self.CategoriaEnum.PRODUCTIVITY,
            self.CategoriaEnum.RESEARCH,
            self.CategoriaEnum.NEWS 
        }

    def __str__(self):
        return f"{self.tipo}"
        

class Website(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(null=False, max_length=250)
    url = models.URLField(null=False, max_length=2000)
    resumen = models.CharField(null=False, max_length=250, default="")
    calificacionPromedio = models.DecimalField(null=False, decimal_places=2, max_digits=4)
    gradoVeracidadPromedio = models.DecimalField(null=False, decimal_places=2, max_digits=4)
    categoria = models.ForeignKey(Categoria, null=False, on_delete=models.CASCADE)
    autor = models.CharField(null=True, max_length=50)
    fecha = models.DateField(null=True)
    disenoPromedio = models.DecimalField(null=False, decimal_places=2, max_digits=4, default=0)
    usabilidadPromedio = models.DecimalField(null=False, decimal_places=2, max_digits=4, default=0)
    
    def __str__(self):
        return f"{self.nombre}"

class ReviewMetadata(models.Model):
    website = models.OneToOneField(Website, on_delete=models.CASCADE, primary_key=True)
    numReviews = models.IntegerField(null=False, default=0)
    sumaCalificacion = models.IntegerField(null=False, default=0)
    sumaVeracidad = models.IntegerField(null=False, default=0)
    numReviewsOptionalParams = models.IntegerField(null=False, default=0)
    sumaDiseno = models.IntegerField(null=False, default=0)
    sumaUsabilidad = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f"Review Metadata de: {self.website}"

class DatosCategoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    website = models.OneToOneField(Website, null=False, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Categoria, null=False, on_delete=models.CASCADE)
    cantReviews = models.IntegerField(null=False, default=0)

    class Meta:
        unique_together = ('website', 'tipo')

    def __str__(self):
        return f"Datos de Website: {self.website}"
