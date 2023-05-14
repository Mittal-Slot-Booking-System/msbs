from django.db import models

# Create your models here.
class FileUp(models.Model):
    file = models.FileField()
    