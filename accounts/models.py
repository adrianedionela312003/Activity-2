from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=6,
        choices=(
            ('vendor', 'Vendor'),
            ('user', 'User'),
        ),
        default='user'
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    valid_id = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username