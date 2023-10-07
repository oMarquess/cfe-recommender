from django.contrib import admin

# Register your models here.
from . models import Products

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'calculate_ratings_count']
    readonly_fields = ['calculate_ratings_count', 'calculate_ratings_avg']
admin.site.register(Products, ProductAdmin)