from django.conf import settings
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('Category', CategoryViewSet)
router.register('Books', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
]