from django import forms
from .models import Usuario, TipoUsuario
class SignupForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')

    def signup(self, request, user):
        tipo = TipoUsuario.objects.filter(tipo="FREE").first()
        user.tipo = tipo
        user.save()
        usuario = Usuario.objects.create(user=user, 
                                        nombre=self.cleaned_data['name'], 
                                        puntos = 0, 
                                        fechaVencimiento=None, 
                                        tipoUsuario=tipo)
        usuario.save()