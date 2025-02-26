from django.contrib.auth.models import AbstractUser
from utils.unique_id_creation import create_id
from django.db import models


class CustomUser(AbstractUser):
    id = models.CharField(primary_key=True, max_length=64, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = create_id(self.username)
        return super().save(*args, **kwargs)
