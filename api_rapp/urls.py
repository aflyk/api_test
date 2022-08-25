from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'phones', views.PhoneAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('alldata', views.PhoneAllData.as_view())
]
