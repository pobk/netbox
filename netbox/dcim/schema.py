from drf_spectacular.extensions import (
    OpenApiSerializerFieldExtension
)
from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import extend_schema
from drf_spectacular.plumbing import build_basic_type
from drf_spectacular.types import OpenApiTypes


class FixTimeZoneSerializerField(OpenApiSerializerFieldExtension):
    target_class = 'timezone_field.rest_framework.TimeZoneSerializerField'

    def map_serializer_field(self, auto_schema, direction):
        return build_basic_type(OpenApiTypes.STR)
