from django.db import models

# Create your models here.

class ChatGPTResponse(models.Model):
    response = models.TextField()

    class Meta:
        db_table = 'chatgptresponse'  # Matches your table name

    def __str__(self):
        return self.response