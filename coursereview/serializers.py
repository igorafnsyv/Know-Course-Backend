from rest_framework import serializers
from .models import Course, Review


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['code', 'title', 'description', 'prerequisites']
        extra_kwargs = {'prerequisites': {'required': False}}

    def get_fields(self):
        fields = super(CourseSerializer, self).get_fields()
        fields['prerequisites'] = CourseSerializer(many=True)
        return fields


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['course', 'date_created', 'rating', 'year_taken', 'subclass', 'professor', 'assessment', 'grade',
                  'review', 'suggestions']