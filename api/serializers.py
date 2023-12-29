from rest_framework_gis import serializers
from home.models import Natoshi


class NatoshiSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Natoshi
        geo_field = "geom"
        fields = "__all__"  