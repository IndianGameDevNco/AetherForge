from django.http import HttpResponseForbidden

class AdminAccessMiddleware:
    ALLOWED_IPS = ['127.0.0.1']  # Add allowed IP addresses here

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.META['REMOTE_ADDR'] not in self.ALLOWED_IPS:
            return HttpResponseForbidden("You are not allowed to access this page.")
        return self.get_response(request)