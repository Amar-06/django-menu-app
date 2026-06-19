from django.db import models

# Create your models here.
class food(models.Model):
    dish=models.CharField( max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    image=models.CharField(max_length=500 , default="https://cdn-icons-png.freepik.com/512/14228/14228079.png" )
    def __str__(self):
        return self.dish
    
