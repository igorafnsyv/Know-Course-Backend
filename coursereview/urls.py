from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('courses', views.CourseViewSet, basename='courses')


urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.UserProfileList.as_view(), name='users'),
    path('users/<str:username>/', views.UserProfileDetail.as_view(), name='user')

]
