from django.db import models

# Create your models here.
class List(models.Model):
    subject = models.CharField(max_length=200)
    details = models.TextField(max_length=1000, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.subject