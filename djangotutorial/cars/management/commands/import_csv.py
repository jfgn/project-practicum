import csv
from datetime import datetime
from decimal import Decimal
from django.core.management.base import BaseCommand
from cars.models import Car  # Изменено на соответствующую модель

class Command(BaseCommand):
    help = "Импорт данных из CSV-файла в модель Car"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Путь к CSV-файлу")

    def handle(self, *args, **options):
        file_path = options["file_path"]
        
        def parse_value(value, field_type):
            """ Преобразует строковые значения из CSV в нужные типы или None, если значение пустое """
            value = value.strip()
            
            if value in ("", "NULL", "None", "NaT", "Unknown"):  # Обрабатываем "Unknown"
                return None
            
            if field_type == int:
                try:
                    return int(value.replace(',', ''))  # Убираем запятые и преобразуем в число
                except ValueError:
                    return None  # Если не удалось преобразовать, возвращаем None
            
            if field_type in (float, Decimal):
                return Decimal(value.replace(',', '').replace('$', ''))  # Убираем запятые и знак $

            if field_type == datetime.date:
                return datetime.strptime(value, "%d-%b-%y").date()  # Парсим дату

            return value


        with open(file_path, newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            print(reader.fieldnames)
            cars = []  # Список объектов для массового создания

            for row in reader:
                car = Car(
                    make=parse_value(row["Make"], str),
                    model=parse_value(row["Model"], str),
                    year=parse_value(row["Year"], int),
                    price=parse_value(row["Price"], Decimal),
                    mileage=parse_value(row["Mileage"], int),
                    body_type=parse_value(row["Body Type"], str),
                    cylinders=parse_value(row["Cylinders"], int),
                    transmission=parse_value(row["Transmission"], str),
                    fuel_type=parse_value(row["Fuel Type"], str),
                    color=parse_value(row["Color"], str),
                    location=parse_value(row["Location"], str),
                    description=parse_value(row["Description"], str),
                )
                cars.append(car)

            Car.objects.bulk_create(cars)
            self.stdout.write(self.style.SUCCESS(f"Успешно импортировано {len(cars)} записей из {file_path}"))
