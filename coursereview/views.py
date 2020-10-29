from django.http import JsonResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import action

from .models import UserProfile, Course, Review
from .serializers import UserProfileSerializer, CourseSerializer, ReviewSerializer


class UserProfileList(generics.ListCreateAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'username'


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'code'

    @action(detail=True)
    def reviews(self, request, code):
        query_set = Review.objects.filter(course__code=code)
        serializer = ReviewSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)



