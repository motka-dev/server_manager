from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_json_settings(json_data):
   print(json_data, type(json_data))
