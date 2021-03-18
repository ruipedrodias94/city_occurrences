from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
#router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
#router.register(r'occurrences', views.Occurrences)#
# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    path('occurrences/', views.OccurrenceList.as_view()),
    path('occurrence/<int:pk>/', views.OccurrenceDetail.as_view()),
]
