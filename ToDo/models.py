from django.db import models

# Create your models here.
class TodoDB(models.Model):
        date=models.DateTimeField()
        text=models.CharField(max_length=100)

        def __str__(self):
            return self.text