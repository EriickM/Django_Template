from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} {self.description}'

