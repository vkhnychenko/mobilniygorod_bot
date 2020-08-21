from django.contrib import admin
from .models import ManualItem, ManualCategory

admin.site.register(ManualItem)
admin.site.register(ManualCategory)