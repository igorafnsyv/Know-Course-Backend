from django.urls import path, include
from . import views
from .views import CourseViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('courses', CourseViewSet, basename='courses')


urlpatterns = [
    # path('', views.get_all_courses, name='all_courses'),
    path('', include(router.urls))
]
