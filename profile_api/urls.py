from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profile_api import views

router = DefaultRouter()
router.register(r'view-set', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('', views.HelloApiView.as_view(), name='Hello Api View'),
    path('', include(router.urls))
]