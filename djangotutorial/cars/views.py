from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from cars.models import Car
from cars.serializers import CarsSerializer
from .renderers import CSVRenderer  # Импортируем CSV-рендерер

class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer
    renderer_classes = [JSONRenderer, CSVRenderer]  # Добавляем поддержку CSV