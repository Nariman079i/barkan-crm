from rest_framework.serializers import *
from barkan.models import *


class ServiceSeializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class HistorySeializer(ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"


class CustomerSeializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class GuideSeializer(ModelSerializer):
    class Meta:
        model = Guide
        fields = "__all__"