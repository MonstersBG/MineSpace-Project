from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models
from .validators import validate_alphabetic


# Create your models here.


class AppUser(auth_models.AbstractUser):
    roles = (("user", "User"), ("admin", "Site Admin"))

    email = models.EmailField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=30,
                                  validators=(MinLengthValidator(2), validate_alphabetic))
    last_name = models.CharField(max_length=30,
                                 validators=(MinLengthValidator(2), validate_alphabetic))

    role = models.CharField(max_length=20, choices=roles, default='user')
    profile_picture = models.URLField(null=True, blank=True)

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
