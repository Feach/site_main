from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "price", "create_at", "id"]
    list_filter = ["id", ]
    save_as = True
    save_on_top = True


class CategoryAdmin(MPTTModelAdmin):
    list_display = ["name", "id"]
    list_filter = ["id", ]
    save_as = True
    save_on_top = True


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Reviews)





