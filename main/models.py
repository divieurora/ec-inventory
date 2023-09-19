from django.db import models

# Create your models here.
class Item(models.Model):
    CATEGORY_CHOICES = (
        ('Top', 'Top'),
        ('Bottom', 'Bottom'),
        ('Dress', 'Dress'),
        ('Extras', 'Extras'),
        ('Accessories', 'Accessories'),
        ('Footwear', 'Footwear'),
    )

    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='top')

    def cat(self):
        return f"{self.name} is a {self.category}"