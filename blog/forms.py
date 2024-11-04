from django import forms
from .models import Profile, Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_pic", "user"]

    # Inicializando com o método __init__ para adicionar classes
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        # Aplicando classes Bootstrap aos campos
        self.fields["bio"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Digite uma breve descrição sobre você",
            }
        )

        self.fields["profile_pic"].widget.attrs.update(
            {"class": "form-control", "style": "padding: 10px;"}
        )

        # Se desejar exibir o campo 'user' como somente leitura
        self.fields["user"].widget.attrs.update(
            {
                "class": "form-control-plaintext",
                "readonly": "readonly",
                "style": "background-color: #EEE3E3; color: #333;",
            }
        )


class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(label="Senha Atual", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Nova Senha", widget=forms.PasswordInput)
    new_password2 = forms.CharField(
        label="Confirmar Nova Senha", widget=forms.PasswordInput
    )


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    new_password1 = forms.CharField(label='Nova Senha', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirmar Nova Senha', widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
