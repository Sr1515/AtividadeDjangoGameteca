from django.contrib.auth import get_user_model
from django.forms.widgets import DateInput
from jogos.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class JogoForm(forms.ModelForm):

    CHOICES = (
        (0, 'Ruim'),
        (1, 'Bom'),
        (2, 'Muito bom'),
        (3, 'Ótimo')
    )

    generos = forms.ModelMultipleChoiceField(queryset=Genero.objects.all(),
                                             widget=forms.CheckboxSelectMultiple)
    plataformas = forms.ModelMultipleChoiceField(queryset=Plataforma.objects.all(),
                                                 widget=forms.CheckboxSelectMultiple)
    avaliacao = forms.ChoiceField(choices=CHOICES)
    capa = forms.ImageField()
    desenvolvedor = forms.ModelChoiceField(
        queryset=Desenvolvedor.objects.all())

    class Meta:
        model = Jogo
        fields = ['nome', 'lancamento', 'generos', 'plataformas', 'avaliacao', 'capa',
                  'desenvolvedor', 'enredo', 'critica']
        widgets = {
            'lancamento': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'type': 'date'
                       }),
        }


class UserCreateUpdate(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username']
