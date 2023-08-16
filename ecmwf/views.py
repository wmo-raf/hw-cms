from django.http import JsonResponse
from proxy.views import proxy_view

from .utils import get_layer_time_values


def ecmwf_get_map_proxy(request):
    base_url = 'https://eccharts.ecmwf.int/wms'

    params = dict(request.GET)

    params.update({"token": "530604a2ed5d28f759c02185beb2ca12"})

    return proxy_view(request, base_url, {"params": params})


def ecmwf_layer_timestamps(request, layer):
    try:
        time_values = get_layer_time_values(layer)
    except Exception:
        time_values = []
        pass

    return JsonResponse({"timestamps": time_values}, )
