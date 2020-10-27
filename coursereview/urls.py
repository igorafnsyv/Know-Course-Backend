from django.urls import path, include
from . import views
from .views import CourseViewSet, ReviewView
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('courses', CourseViewSet, basename='courses')


urlpatterns = [
    path('', include(router.urls)),

]
