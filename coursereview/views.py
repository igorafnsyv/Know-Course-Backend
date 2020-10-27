from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer


# Create your views here.


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'code'

    @action(detail=True)
    def reviews(self, request, code):
        query_set = Review.objects.filter(course__code=code)
        serializer = ReviewSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)



