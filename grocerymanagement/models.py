from django.db import models
from django.contrib.auth.models import User


class GroceryItem(models.Model):

    name = models.CharField(max_length=200)

    CATEGORY_CHOICES = (
        ('vegetables', 'Vegetables'),
        ('fruits', 'Fruits'),
        ('dairy', 'Dairy'),
        ('beverages', 'Beverages'),
        ('snacks', 'Snacks'),
    )

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="fruits")

    price = models.DecimalField(max_digits=10, decimal_places=2)

    quantity = models.PositiveIntegerField()

    expiry_date = models.DateField()

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


