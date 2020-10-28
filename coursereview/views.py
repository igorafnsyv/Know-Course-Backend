from django.http import JsonResponse
from django.views.generic import View
from rest_framework import viewsets, generics
from rest_framework.decorators import action

from .models import User, Course, Review
from .serializers import UserSerializer, CourseSerializer, ReviewSerializer


class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'code'

    @action(detail=True)
    def reviews(self, request, code):
        query_set = Review.objects.filter(course__code=code)
        serializer = ReviewSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)



