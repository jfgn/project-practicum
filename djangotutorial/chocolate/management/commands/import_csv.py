import csv
from datetime import datetime
from decimal import Decimal
from django.core.management.base import BaseCommand
from chocolate.models import Sales  # Изменено на соответствующую модель

class Command(BaseCommand):
    help = "Импорт данных из CSV-файла в модель Sale"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Путь к CSV-файлу")

    def handle(self, *args, **options):
        file_path = options["file_path"]
        
        def parse_value(value, field_type):
            """ Преобразует строковые значения из CSV в нужные типы или None, если значение пустое """
            if value.strip() in ("", "NULL", "None", "NaT"):
                return None
            if field_type == int:
                return int(value.replace(',', '').strip())
            if field_type == float or field_type == Decimal:
                return Decimal(value.replace(',', '').replace('$', '').strip())
            if field_type == datetime.date:
                return datetime.strptime(value.strip(), "%d-%b-%y").date()
            return value.strip()

        with open(file_path, newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            print(reader.fieldnames)
            sales = []  # Список объектов для массового создания

            for row in reader:
                sale = Sales(
                    sales_person=parse_value(row["Sales Person"], str),
                    country=parse_value(row["Country"], str),
                    product=parse_value(row["Product"], str),
                    date=parse_value(row["Date"], datetime.date),
                    amount=parse_value(row["Amount"], Decimal),
                    boxes_shipped=parse_value(row["Boxes Shipped"], int),
                )
                sales.append(sale)

            Sales.objects.bulk_create(sales)
            self.stdout.write(self.style.SUCCESS(f"Успешно импортировано {len(sales)} записей из {file_path}"))
