from django import forms
from django.core import validators
from .models import Proyecto




class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'




class UserRegistrationForm(forms.Form):

    ESTADOS = [('activo', 'ACTIVO'), ('inactivo', 'INACTIVO')]

    nombre = forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    fono = forms.CharField(required=False)
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))


    nombre.widget.attrs['class'] = 'form-control' 
    fono.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'

    def clean_email (self):
        super_clean = super().clean()

        email = super_clean['email']
        if '@' not in email:
            raise forms.ValidationError("El correo debe contener un @")
        return email
    