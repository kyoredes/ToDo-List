from django.contrib.auth.models import AbstractUser
from utils.unique_id_creation import create_id
from django.db import models


class CustomUser(AbstractUser):
    id = models.PositiveBigIntegerField(primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = create_id(self.username)
        return super().save(*args, **kwargs)
