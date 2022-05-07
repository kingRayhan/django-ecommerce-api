from dataclasses import field, fields
from email.headerregistry import Address
from django.contrib import admin

from store.models import Collection, Customer, Order, Product, Promotion


@admin.register(Product, Collection, Promotion, Order, Customer)
class ProductAdmin(admin.ModelAdmin):
    pass
    # list_display = ('title', 'price')
