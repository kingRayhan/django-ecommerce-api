from itertools import product
from pyexpat import model
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField()
    collection = models.ForeignKey(
        to='Collection', on_delete=models.SET_NULL, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    promotions = models.ManyToManyField(
        to='Promotion', blank=True, related_name='products')


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(to='Customer', on_delete=models.CASCADE)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'BRONZE'
    MEMBERSHIP_SILVER = 'SILVER'
    MEMBERSHIP_GOLD = 'GOLD'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE, max_length=10)


class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'PENDING'
    PAYMENT_STATUS_COMPLETE = 'COMPLETED'
    PAYMENT_STATUS_FAIL = 'FAILED'

    PAMENT_STATUS = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Completed'),
        (PAYMENT_STATUS_FAIL, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=255, choices=PAMENT_STATUS, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(to='Customer', on_delete=models.PROTECT)


class OrderItem(models.Model):
    product = models.ForeignKey(to='Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(to='Order', on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    customer = models.ForeignKey(to='Customer', on_delete=models.PROTECT)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(to='Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
