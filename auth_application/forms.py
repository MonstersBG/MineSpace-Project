from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

AppUser = get_user_model()


class RegistrationForm(auth_forms.UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = AppUser
        fields = ["username", "email", "password1", "password2"]

# TODO make placeholders for username, email and passwords until the project defense
