from django.db import models

# Create your models here.
class food(models.Model):
    dish=models.CharField( max_length=50)
    price=models.IntegerField()
    ingrediant=models.TextField()
    def __str__(self):
        return self.dish
