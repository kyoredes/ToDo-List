from django.db import models
from tags.models import Tag
from django.contrib.auth import get_user_model
from utils.unique_id_creation import create_id


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    id = models.CharField(primary_key=True, max_length=64, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = create_id(str(self.user.id))
        return super().save(*args, **kwargs)
