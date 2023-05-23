from django.urls import path, include
from .views import *
from rest_framework import routers
from django.views.decorators.cache import cache_page
from .views import *

router = routers.SimpleRouter()
router.register(r'customers',CustomerAPIView)
router.register(r'history',HistoryAPIView)
router.register(r'services',ServiceAPIView)
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/guide/', GuideListView.as_view()),
    path('api/v1/guide/create/', GuideCreateView.as_view()),
    path('api/v1/guide/<int:pk>/', GuideDetailView.as_view())
]
