from django import forms
from .models import Usuario
class UserForm(forms.ModelForm):
    contrasena = forms.Charfield(widget=forms.PasswordInput)
    class Meta:
        model = Usuario