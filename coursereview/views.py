from rest_framework import generics

from .models import UserProfile, Course, Review
from .serializers import UserProfileSerializer, CourseSerializer, ReviewSerializer


class UserProfileList(generics.ListCreateAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'username'


class CourseList(generics.ListCreateAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'code'


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_object(self):
        return Course.objects.get(code=self.kwargs['code'])


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(course=self.kwargs['code'])


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer

    def get_object(self):
        return Review.objects.get(pk=self.kwargs['pk'], course__code=self.kwargs['code'])

