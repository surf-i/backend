from django.contrib import admin
from .models import Website, Categoria, ReviewMetadata, DatosCategoria
# Register your models here.

admin.site.register(Website)
admin.site.register(Categoria)
admin.site.register(ReviewMetadata)
admin.site.register(DatosCategoria)
