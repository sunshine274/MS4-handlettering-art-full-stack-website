from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Testimony(models.Model):
    created = models.DateTimeField(auto_now_add=True,)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
