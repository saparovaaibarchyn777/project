from email.policy import default
from django.db import models



class Product(models.Model):
    name = models.CharField(max_length= 127 )
    description = models.TextField()
    price = models.IntegerField()
    articul = models.CharField(max_length = 127)

    def __str__(self):
        return self.name



class Cart(models.Model):
    user_name = models.CharField(max_length = 127)
    created_at  = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)
    delivery_address = models.CharField(max_length = 127)


class CartProduct(models.Model):
    product = models.ForeignKey(Product , on_delete = models.CASCADE, related_name = 'cart_products')
    cart = models.ForeignKey(Cart , on_delete = models.CASCADE,related_name = 'cart_products')
    total_price = models.IntegerField(default=0)
    amount = models.IntegerField()


    @property
    def sum_amount(self):
        return self.product.price * self.amount

    def __str__(self):
        return self.product.name
        

