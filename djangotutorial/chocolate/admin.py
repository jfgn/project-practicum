from django.contrib import admin
from .models import Sales

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sales._meta.get_fields()]  # Какие поля показывать
    search_fields = ("country", "product")  # Поля для поиска
    list_filter = ("date", "amount")  # Фильтры сбоку

# Или без декоратора:
# admin.site.register(Sales, SalesAdmin)
