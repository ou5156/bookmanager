from django.db import models

# Create your models here.
class Publisher(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


class Book(models.Model):
    title = models.CharField(max_length=255)
    pub = models.ForeignKey('Publisher',on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField('Book')
    # 不在Author表中生产字段，生产第三张表