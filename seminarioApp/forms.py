from django import forms
from seminarioApp.models import Seminarios


class IngresoForm(forms.ModelForm):
    observaciones = forms.CharField(
        max_length=100, required=False, widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    telefono = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'max': 999999999})
    )

    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    class Meta:
        model = Seminarios
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'organizacion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
        }
