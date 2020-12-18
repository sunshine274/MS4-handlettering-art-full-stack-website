from django.contrib import admin
from .models import Product, Testimony


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'image',
    )

    ordering = ('sku',)


class TestimonyAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'product',
        'text',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Testimony, TestimonyAdmin)
