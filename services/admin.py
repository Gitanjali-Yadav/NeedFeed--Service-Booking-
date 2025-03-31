from django.contrib import admin
from .models import ServiceCategory, Service  # Import your models

# Define admin classes
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Fields to display in the admin list view
    search_fields = ('name',)  # Enable search by name
    list_per_page = 20  # Number of items per page

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Fields to display in the admin list view
    list_filter = ('category',)  # Enable filtering by category
    search_fields = ('name', 'category__name')  # Enable search by name and category name
    list_per_page = 20  # Number of items per page

# Register models with their respective admin classes
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service, ServiceAdmin)