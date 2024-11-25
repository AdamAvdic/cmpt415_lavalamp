from django.db import models

class HuggingFaceRefineWeb(models.Model):
    content = models.TextField(primary_key=True)
    url = models.TextField(max_length=200)  # Field for storing the URL
    timestamp = models.TextField()    # Field for storing the timestamp

    class Meta:
        db_table = 'base_huggingfacerefineweb'  # Match the table name in your database

    def __str__(self):
        return self.content