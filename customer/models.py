from django.db import models

# Create your models here.
class Customer(models.Model):

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Food(models.Model):

    healthy_choices = {
        ("H", "healthy"),
        ("U", "unhealthy"),
    }
    size = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    calories = models.CharField(max_length=250)
    type = models.CharField(choices=healthy_choices, max_length=250, default="healthy")


    def __str__(self):
        return f"{self.size} {self.price} {self.calories} {self.type}"