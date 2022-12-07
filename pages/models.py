from django.db import models
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    date = models.DateField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Book(models.Model):
    book_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')
    price = models.PositiveIntegerField(max_length=6)
    body =  models.TextField()

    def __str__(self):
        return self.book_name