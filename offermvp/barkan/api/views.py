from rest_framework.viewsets import ModelViewSet
from .serializers import *

class CustomerAPIView(ModelViewSet):
    serializer_class = CustomerSeializer
    queryset = Customer.objects.all()


class ServiceAPIView(ModelViewSet):
    serializer_class = ServiceSeializer
    queryset = Service.objects.all()


class HistoryAPIView(ModelViewSet):
    serializer_class = HistorySeializer
    queryset = History.objects.all()


class GuideAPIView(ModelViewSet):
    serializer_class = GuideSeializer
    queryset = Guide.objects.all()
