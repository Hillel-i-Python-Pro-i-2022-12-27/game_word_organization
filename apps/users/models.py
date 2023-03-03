from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # pass
    avatar = models.ImageField(
        max_length=300,
        upload_to="contacts/contact/avatar/",
        blank=True,
        null=True,
        default=None,
    )
