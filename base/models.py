from django.db import models

# Create your models here.

class HuggingFaceRefineWeb(models.Model):
    content = models.TextField()

class Meta:
    db_table = 'huggingface-refineweb'

def __str__(self):
    return self.content