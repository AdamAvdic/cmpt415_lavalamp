from django.db import models

class HuggingFaceRefineWeb(models.Model):
    content = models.TextField()
    url = models.TextField(max_length=200)  # Field for storing the URL
    timestamp = models.TextField()    # Field for storing the timestamp

    class Meta:
        db_table = 'huggingface-refineweb'  # Match the table name in your database

    def __str__(self):
        return self.content