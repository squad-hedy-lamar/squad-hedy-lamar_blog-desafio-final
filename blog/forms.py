from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        img = forms.ImageField(required=False)
        fields = ['bio', 'profile_pic', 'user']

class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(label='Senha Atual', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Nova Senha', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirmar Nova Senha', widget=forms.PasswordInput)

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
