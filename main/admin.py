from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "price", "create_at"]
    save_as = True
    save_on_top = True


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Reviews)





