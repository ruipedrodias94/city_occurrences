from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('occurrences/', views.OccurrenceList.as_view()),
    path('occurrence/<int:pk>/', views.OccurrenceDetail.as_view()),
]
