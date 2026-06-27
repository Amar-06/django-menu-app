from django.db import models
from django.contrib.auth.models import User
from django.urls import  reverse
# Create your models here.
class food(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    dish=models.CharField( max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    image=models.CharField(max_length=500 , default="https://cdn-icons-png.freepik.com/512/14228/14228079.png" )
    def __str__(self):
        return self.dish
    def get_absolute_url(self):
        return reverse('food:Food_Detail',kwargs={"pk":self.pk})
    
