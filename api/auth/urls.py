from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path('login/', views.LoginGenericAPIView.as_view()),
    path('', include(router.urls)),
]