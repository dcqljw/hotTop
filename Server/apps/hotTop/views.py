from django.http import JsonResponse
from rest_framework.decorators import api_view

from apps.hotTop import models
from apps.hotTop.serializers import HotSerializers


@api_view(["GET"])
def hot(request):
    """
    :param request:
    :return:
    """
    source = request.GET.get("source")
    objects_filter = models.HotTop.objects.filter(source=source)
    idx = getIdx(source)
    topList = list(models.HotTop.objects.filter(source=source).order_by("-id").limit(idx))[::-1]
    hot_serializers = HotSerializers(topList, many=True)
    context = {
        "data": hot_serializers.data
    }
    return JsonResponse(context, safe=False, status=200)


def getIdx(source):
    return models.HotTop.objects.filter(source=source).order_by("-id").first().idx
