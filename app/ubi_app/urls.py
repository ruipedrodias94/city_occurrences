from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('ubi_app.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
