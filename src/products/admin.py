from django.contrib import admin

# Register your models here.
from . models import Products

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'rating_avg', 'rating_last_updated', 'rating_count']
    readonly_fields = ['rating_avg','rating_count', 'rating_avg_display']
admin.site.register(Products, ProductAdmin)