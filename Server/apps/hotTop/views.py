from django.http import JsonResponse
from rest_framework.decorators import api_view

from apps.hotTop import models
from apps.hotTop.serializers import HotSerializers, HotDateSerializers
from utils.UrlSign import verify
import time


@api_view(["GET"])
def hot(request):
    """
    :param request:
    :return:
    """
    source = request.GET.get("source")
    context = {}
    try:
        idx = models.HotTop.objects.filter(source=source).order_by("-id").first().idx
        topList = list(models.HotTop.objects.filter(source=source).order_by("-id").limit(idx))[::-1]
        hot_serializers = HotSerializers(topList, many=True)
        context["title"] = source
        context["data"] = hot_serializers.data
        return JsonResponse(context, safe=False)
    except Exception:
        context["msg"] = "error"
        return JsonResponse(context, safe=False, status=404)


def getIdx(source):
    return models.HotTop.objects.filter(source=source).order_by("-id").first().idx


@api_view(["POST"])
def test(request):
    source = request.GET.get("source")
    t = request.POST.get("t")
    sign = request.POST.get("sign")
    context = {}
    if verify(t=t, sign=sign):
        dateList = list(models.HotTopDate.objects.filter(source=source))
        date_serializers = HotDateSerializers(dateList, many=True)
        context = {
            "data": date_serializers.data
        }
        return JsonResponse(context, safe=False)
    else:
        context["data"] = []
        context["msg"] = "error"
        return JsonResponse(context, safe=False, status=201)


# TODO 获取所有数据
def get_all_hot(request):
    pass
