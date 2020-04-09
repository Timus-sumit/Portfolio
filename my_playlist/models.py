from django.db import models

# Create your models here.
class My_playlist(models.Model):
    title= models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    summary=models.TextField(max_length=400)
    url=models.CharField(max_length=100, default='#')

    def __str__(self):
        return self.title

class Latest(models.Model):
    image=models.ImageField(upload_to="images/")
    title=models.CharField(max_length=100)
    url=models.TextField(max_length=100, default="#")
