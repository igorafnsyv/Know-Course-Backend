from django.urls import path, include
from . import views
from .views import CourseViewSet, UserList
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('courses', CourseViewSet, basename='courses')


urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.UserList.as_view(), name='users')

]
