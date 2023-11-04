from django.contrib import admin
from .models import *

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ["title", "price", "category"]

admin.site.register(Product,AdminProduct)

class AdminCategory(admin.ModelAdmin):
    list_display = ["name","date_added"]

admin.site.register(Category,AdminCategory)
