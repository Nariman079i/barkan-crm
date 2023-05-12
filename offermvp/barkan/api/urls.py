from django.urls import path, include
from .views import *
from rest_framework import routers
from django.views.decorators.cache import cache_page
from .views import *

router = routers.SimpleRouter()
router.register(r'customers',CustomerAPIView)
router.register(r'history',HistoryAPIView)
router.register(r'guide', GuideAPIView),
router.register(r'services',ServiceAPIView)
urlpatterns = [
    path('api/v1/', include(router.urls))
]
