from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre usuario ya existe")
    
    def clean(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            self.add_error("password2", "Las contraseñas no coinciden")
    def save(self):
        return User.objects.create_user(
            username=self.cleaned_data.get("username"),
            email = self.cleaned_data.get("email"),
            password= self.cleaned_data.get("password")
        )
