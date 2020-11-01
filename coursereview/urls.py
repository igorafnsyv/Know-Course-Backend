from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('users/<str:username>/', views.UserProfileDetail.as_view(), name='user'),
    path('users/', views.UserProfileList.as_view(), name='users'),
    path('courses/<str:code>/reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review'),
    path('courses/<str:code>/reviews/', views.ReviewList.as_view(), name='reviews'),
    path('courses/<str:code>/', views.CourseDetail.as_view(), name='course'),
    path('courses/', views.CourseList.as_view(), name='courses')
]
