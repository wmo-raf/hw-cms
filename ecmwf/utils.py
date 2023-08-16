from datetime import datetime

from isodate import parse_duration
from owslib.wms import WebMapService


def get_layer_time_values(layer, base_url, token):
    params = {
        "layers": layer,
        "token": token
    }

    query_string = "&".join([f"{key}={value}" for key, value in params.items()])

    full_url = f"{base_url}?{query_string}"

    wms = WebMapService(full_url, version='1.3.0')

    wms_layers = list(wms.contents)
    timestamps = []

    for layer in wms_layers:
        if layer == layer:
            time = wms[layer].dimensions.get("time")

            if time:
                values = time.get("values")
                parts = values[1].split("/")
                start_time = datetime.strptime(parts[0], "%Y-%m-%dT%H:%M:%SZ")
                end_time = datetime.strptime(parts[1], "%Y-%m-%dT%H:%M:%SZ")
                duration_str = parts[2]
                duration = parse_duration(duration_str)

                current_time = start_time
                timestamps = []

                while current_time < end_time:
                    timestamps.append(current_time.strftime("%Y-%m-%dT%H:%M:%SZ"))
                    current_time += duration
            break

    return timestamps
