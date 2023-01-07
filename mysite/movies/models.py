from django.db import models

# Create your models here.

class MovieData(models.Model):
  name= models.CharField(max_length=200)
  duration = models.FloatField()
  rating = models.FloatField()
  category = models.CharField(max_length=100, default="action")
  image = models.ImageField(upload_to="images/", default="images/None/noimg.png")
  
  
  def __str__(self) -> str:
    return self.name