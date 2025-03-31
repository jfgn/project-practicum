from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100, verbose_name="Марка")
    model = models.CharField(max_length=100, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год выпуска")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена ($)")
    mileage = models.IntegerField(verbose_name="Пробег (км)")
    body_type = models.CharField(max_length=100, verbose_name="Тип кузова")
    cylinders = models.IntegerField(verbose_name="Количество цилиндров", null=True, blank=True)
    transmission = models.CharField(max_length=100, verbose_name="Трансмиссия")
    fuel_type = models.CharField(max_length=100, verbose_name="Тип топлива")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    location = models.CharField(max_length=100, verbose_name="Местоположение")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        db_table = "cars"  # Имя таблицы в базе данных
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"