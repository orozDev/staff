from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .yasg import urlpatterns as url_doc
from . import views

router = DefaultRouter()
router.register('posts', views.PostModelViewSet)

urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('', include(router.urls))
]

urlpatterns += url_doc