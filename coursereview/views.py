from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from .models import Course

# TODO: add Django rest for JSON response


def get_all_courses(request):
    data = list(Course.objects.values())
    return JsonResponse(data, safe=False)

