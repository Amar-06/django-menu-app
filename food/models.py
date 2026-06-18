from django.db import models

# Create your models here.
class food(models.Model):
    dish=models.CharField( max_length=50)
    price=models.IntegerField()
    ingrediant=models.TextField()
    image=models.CharField(max_length=500 , default="https://cdn-icons-png.freepik.com/512/14228/14228079.png" )
    def __str__(self):
        return self.dish
    
class Hostel(models.Model):
    hostel_name = models.CharField(max_length=100)
    hostel_code = models.CharField(max_length=20)

    def __str__(self):
        return self.hostel_name
    


class Menu(models.Model):

    DAY_CHOICES = [
        ('MON','Monday'),
        ('TUE','Tuesday'),
        ('WED','Wednesday'),
        ('THU','Thursday'),
        ('FRI','Friday'),
        ('SAT','Saturday'),
        ('SUN','Sunday'),
    ]

    MEAL_CHOICES = [
        ('BREAKFAST','Breakfast'),
        ('LUNCH','Lunch'),
        ('SNACKS','Snacks'),
        ('DINNER','Dinner'),
    ]

    day = models.CharField(max_length=10, choices=DAY_CHOICES)

    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)

    menu_items = models.TextField()

    special = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.day} - {self.meal_type}"
