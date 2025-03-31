from django.db import models

class Sales(models.Model):
    sales_person = models.CharField(max_length=200, verbose_name="Продавец")
    country = models.CharField(max_length=100, verbose_name="Страна")
    product = models.CharField(max_length=200, verbose_name="Название продукта")
    date = models.DateField(verbose_name="Дата продажи")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма продажи ($)")
    boxes_shipped = models.IntegerField(verbose_name="Количество отправленных коробок")

    class Meta:
        db_table = "chocolate_sales"  # Имя таблицы в базе данных
        verbose_name = "Продажа шоколада"
        verbose_name_plural = "Продажи шоколада"

    def __str__(self):
        return f"{self.sales_person} - {self.product} ({self.date})"