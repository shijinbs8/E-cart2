from django.contrib import admin
from .models import Category,Products,Cart,CartProduct,Customer
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','available','description']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Products,ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)

