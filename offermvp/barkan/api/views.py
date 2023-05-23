from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django.db.models import Q
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView, CreateAPIView
class CustomerAPIView(ModelViewSet):
    serializer_class = CustomerSeializer
    queryset = Customer.objects.all()


class ServiceAPIView(ModelViewSet):
    serializer_class = ServiceSeializer
    queryset = Service.objects.all()


class HistoryAPIView(ModelViewSet):
    serializer_class = HistorySeializer
    queryset = History.objects.all()

    
class GuideListView(ListAPIView):
    serializer_class = GuideSeializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        sort = self.request.query_params.get('sort')
        if search:
            return Guide.objects.filter(
                Q(surname__icontains=search) |
                Q(name__icontains=search) |
                Q(patronymic__icontains=search) |
                Q(tel__icontains=search))
        elif sort:
            return Guide.objects.all().order_by(sort)
        else:
            return Guide.objects.all()
    
class GuideCreateView(CreateAPIView):
    serializer_class = GuideSeializer
    queryset = Guide.objects.all()
    
class GuideDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GuideSeializer
    queryset = Guide.objects.all()

# class GuideAPIView(ModelViewSet):
#     serializer_class = GuideSeializer

#     def get_queryset(self):
#         experience = self.request.query_params('experience') 
#         salary = self.request.query_params('salary') 
#         if experience == "all" and salary == 'all':
#             return Guide.objects.all()
#         return Guide.objects.filter(Q(experience=experience) | Q(salary=salary))
