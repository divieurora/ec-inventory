from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=100, null=True, blank=True)

    def cat(self):
        return f"{self.name} is a {self.category}"