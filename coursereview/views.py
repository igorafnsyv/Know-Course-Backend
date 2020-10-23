from rest_framework import viewsets
from .serializers import CourseSerializer
# Create your views here.

from .models import Course
from rest_framework import viewsets

from .models import Course
from .serializers import CourseSerializer


# Create your views here.

# TODO: add Django rest for JSON response


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


