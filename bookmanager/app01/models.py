from django.db import models

# Create your models here.
class Publisher(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

class Book(models.Model):
    title = models.CharField(max_length=255)
    pub = models.ForeignKey('Publisher',on_delete=models.CASCADE)
