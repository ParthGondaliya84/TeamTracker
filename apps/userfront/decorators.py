from functools import wraps
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate

def token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        token = request.COOKIES.get('accessToken')  # Or retrieve from headers
        if not token:
            return HttpResponseRedirect(reverse('login'))  # Redirect to login page
        # Optionally, verify the token if needed
        return view_func(request, *args, **kwargs)
    return _wrapped_view
