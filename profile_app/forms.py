from django import forms
from django.contrib.auth import get_user_model

AppUser = get_user_model()


class UserEditForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ["username", "email", "first_name", "last_name", "profile_picture", "role"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields["username"].disabled = True
        self.fields["username"].widget.attrs["placeholder"] = "Username: " + self.instance.username
        self.fields["role"].disabled = True
        self.fields["role"].widget.attrs["placeholder"] = "Role: " + self.instance.role


class UserDeleteForm(forms.ModelForm):
    pass
# TODO make a base UserForm and add pretty much the same parameters here, but make it so no fields could be touched
