from django.contrib import admin
from .models.customer import Customer
from .models.products import Product
from .models.orders import Order
from .models.category import Category, Stock



# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Stock)


