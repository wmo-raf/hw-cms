from datetime import datetime

from isodate import parse_duration
from owslib.wms import WebMapService


def get_layer_time_values(layer):
    base_url = "https://eccharts.ecmwf.int/wms/?"

    base_url = base_url + "&token=530604a2ed5d28f759c02185beb2ca12"
    base_url = base_url + f"&layers={layer}"

    wms = WebMapService(base_url, version='1.3.0')

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
