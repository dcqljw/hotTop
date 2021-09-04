from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class HeadersMD(MiddlewareMixin):
    def process_request(self, request):
        try:
            user_agent = request.META["HTTP_USER_AGENT"]
            if 'Postman' in user_agent:
                return JsonResponse({"code": "error"})
            return
        except Exception:
            return JsonResponse({"code": "error"})
