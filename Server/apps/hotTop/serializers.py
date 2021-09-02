from rest_framework_mongoengine import serializers
from apps.hotTop.models import HotTop, HotTopDate


class HotSerializers(serializers.DocumentSerializer):
    class Meta:
        model = HotTop
        fields = ["idx", "title", "url", "date", "source"]


class HotDateSerializers(serializers.DocumentSerializer):
    class Meta:
        model = HotTopDate
        fields = ["date", "source"]
