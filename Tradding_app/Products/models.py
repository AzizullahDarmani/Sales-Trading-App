from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name



# class Product(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
#     name = models.CharField(max_length=200, blank=False)
#     description = models.TextField(null=True, blank=True)
#     price = models.DecimalField(max_digits=30, decimal_places=5)
#     image = models.ImageField(upload_to='profiles/',default='profiles/default.png', blank=True, null=True)

#     def __str__(self):
#         return self.name

