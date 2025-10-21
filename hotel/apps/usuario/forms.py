from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email


class LoginForm(forms.Form):
    login = forms.CharField(label="Usuario o Email")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        login_input = cleaned_data.get('login')
        password = cleaned_data.get('password')

        user = None

        if login_input and password:
            try:
                user_obj = User.objects.get(email=login_input)
                username = user_obj.username
            except User.DoesNotExist:
                username = login_input

            user = authenticate(username=username, password=password)

            if user is None:
                raise forms.ValidationError("Credenciales inválidas.")
            if not user.is_active:
                raise forms.ValidationError("Cuenta inactiva.")

        self.user = user
        return cleaned_data

    def get_user(self):
        return self.user

        return self.user