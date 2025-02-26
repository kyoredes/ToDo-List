from django.db import models
from utils.unique_id_creation import create_id


class Tag(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=64)
    name = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = create_id(self.name)

        return super().save(*args, **kwargs)
