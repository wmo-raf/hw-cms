from django.urls import path

from .views import ecmwf_get_map_proxy, ecmwf_layer_timestamps

urlpatterns = [
    path('api/ecmwf-hres/', ecmwf_get_map_proxy, name="ecmwf-get-map-proxy"),
    path('api/ecmwf-hres/time-values/<str:layer>/', ecmwf_layer_timestamps, name="ecmwf-layer-timestamps"),
]
