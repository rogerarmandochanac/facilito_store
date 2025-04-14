from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    error_css_class = 'text-danger'
    username = forms.CharField(required=True, min_length=4, 
                                max_length=20, widget=forms.TextInput(
                                    {'class':'form-control'}
                                ))
    email = forms.EmailField(required=True, widget=forms.EmailInput({'class':'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput({'class':'form-control'}))
    password2 = forms.CharField(label="Confirmar password", required=True, widget=forms.PasswordInput({'class':'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya existe.")
            
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electronico ya existe.")
        
        return email
    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get("password") != cleaned_data.get("password2"):
            self.add_error("password2", "Las contraseñas no coinciden")
    
    def save(self):
        return User.objects.create_user(
            username = self.cleaned_data.get("username"),
            email = self.cleaned_data.get("email"),
            password = self.cleaned_data.get("password")
        )