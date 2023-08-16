from django.http import JsonResponse
from proxy.views import proxy_view

from .models import EcmwfSettings
from .utils import get_layer_time_values


def ecmwf_get_map_proxy(request):
    ec_settings = EcmwfSettings.for_request(request)
    base_url = ec_settings.eccharts_wms_url
    params = dict(request.GET)
    if ec_settings.eccharts_api_token:
        params.update({"token": ec_settings.eccharts_api_token})
    return proxy_view(request, base_url, {"params": params})


def ecmwf_layer_timestamps(request, layer):
    ec_settings = EcmwfSettings.for_request(request)
    base_url = ec_settings.eccharts_wms_url
    token = ec_settings.eccharts_api_token
    try:
        time_values = get_layer_time_values(layer, base_url, token)
    except Exception:
        time_values = []
        pass

    return JsonResponse({"timestamps": time_values}, )
