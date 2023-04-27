from django.contrib import admin
from menu.models import Menu, Category, Product

admin.site.register(Menu)
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'available']
