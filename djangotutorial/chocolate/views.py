from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from chocolate.models import Sales
from chocolate.serializers import ChocolateSerializer
from .renderers import CSVRenderer  # Импортируем CSV-рендерер

class SalesListView(ListAPIView):
    queryset = Sales.objects.all()
    serializer_class = ChocolateSerializer
    renderer_classes = [JSONRenderer, CSVRenderer]  # Добавляем поддержку CSV