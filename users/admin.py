from django.contrib import admin
from .models import Usuario, Review, TipoUsuario
# Register your models here.

admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Review)