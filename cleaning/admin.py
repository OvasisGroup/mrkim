from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Category, SubCategory

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'header_image', 'image')
    search_fields = ('name',)

admin.site.register(Category, ImportExportModelAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)

admin.site.register(SubCategory, ImportExportModelAdmin)