from django import forms
from pymongo.errors import BulkWriteError
from .models import Usuario, TipoUsuario
class SignupForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')

    def signup(self, request, user):
        user.save()
        tipo = TipoUsuario.objects.filter(tipo="FREE").first()
        try:
            usuario = Usuario.objects.create(user=user, 
                                            nombre=self.cleaned_data['name'], 
                                            puntos = 0, 
                                            fechaVencimiento="1900-01-01", 
                                            tipoUsuario=tipo)
            usuario.save()
        except BulkWriteError:
            return False