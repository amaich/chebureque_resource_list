from django.contrib import admin
from .models import ResourceModel

@admin.register(ResourceModel)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'description']
# Register your models here.
