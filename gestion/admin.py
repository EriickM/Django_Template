from django.contrib import admin

from gestion.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    fields = ('title',)
admin.site.register(Category, CategoryAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category')
