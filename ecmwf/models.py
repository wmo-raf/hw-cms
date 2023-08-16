from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting
from wagtail.contrib.settings.registry import register_setting


@register_setting(icon="cog")
class EcmwfSettings(BaseSiteSetting):
    eccharts_wms_url = models.URLField(default="https://eccharts.ecmwf.int/wms")
    eccharts_api_token = models.CharField(max_length=255)

    panels = [
        FieldPanel("eccharts_wms_url"),
        FieldPanel("eccharts_api_token")
    ]
