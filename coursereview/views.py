
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from django.http import HttpResponse
from django.contrib.auth import authenticate

from .custom_permissions import *
from .models import UserProfile, Course, Review
from .serializers import UserProfileSerializer, CourseSerializer, ReviewSerializer

import json
from .custom_auth import BearerTokenAuthentication


class UserLoginVerifier(APIView):

    def post(self, request, format=None):
        user_upload = json.loads(request.body)
        user = authenticate(username=user_upload['username'], password=user_upload['password'])
        if user:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)


class UserProfileList(generics.ListCreateAPIView):

    # only admin should be able to see the Student List
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [BasicAuthentication, BearerTokenAuthentication]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):

    # only account owner should be able to view profile information
    permission_classes = [IsOwner]
    authentication_classes = [BasicAuthentication, BearerTokenAuthentication]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'username'


class CourseList(generics.ListCreateAPIView):

    # only admin can create Course object
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [BasicAuthentication, BearerTokenAuthentication]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'code'


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):

    # Only admin can update the course info
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [BasicAuthentication, BearerTokenAuthentication]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_object(self):
        return Course.objects.get(code=self.kwargs['code'])


class ReviewList(generics.ListCreateAPIView):

    # Everyone can view the reviews, but must be logged in to write a review
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication, BearerTokenAuthentication]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(course=self.kwargs['code'])

    def perform_create(self, serializer):
        serializer.save(author=UserProfile.objects.get(username=self.request.user.username),
                        course=Course.objects.get(code=self.kwargs['code']))


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):

    # Everyone who is logged in should be able to read the reviews, but only owner can update it
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [BasicAuthentication, BearerTokenAuthentication]
    serializer_class = ReviewSerializer

    def get_object(self):
        return Review.objects.get(pk=self.kwargs['pk'], course__code=self.kwargs['code'])

