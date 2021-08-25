from rest_framework_mongoengine import serializers
from apps.hotTop.models import HotTop


class HotSerializers(serializers.DocumentSerializer):
    class Meta:
        model = HotTop
        fields = ["idx", "title", "url", "date", "source"]
