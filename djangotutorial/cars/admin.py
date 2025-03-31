from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.get_fields()]  # Какие поля показывать
    search_fields = ("model", "make")  # Поля для поиска
    list_filter = ("color", "fuel_type")  # Фильтры сбоку

# Или без декоратора:
# admin.site.register(Car, CarAdmin)
