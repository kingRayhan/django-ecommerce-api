

from django.http import HttpResponse
from django.urls import path
from json import dumps as JSONDump


def test(request):
    data = {
        "message": "Hello wold"
    }
    return HttpResponse(content=JSONDump(data), content_type="application/json")


urlpatterns = [
    path('', test),
]
