from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    class Role(models.TextChoices):
        ORGANIZATION = "ORGANIZATION", "Organization"
        ADMIN = "ADMIN", "Admin"

    email = models.EmailField(unique=True, verbose_name="Email address")

    first_name = models.CharField(max_length=100, verbose_name="First name")

    last_name = models.CharField(max_length=100, verbose_name="Last name")

    phone_number = models.CharField(
        max_length=20, blank=True, verbose_name="Phone number"
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.ORGANIZATION,
        verbose_name="User role",
    )

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
