from rest_framework import serializers
from .models import *
from django.db.models import Avg
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['username', 'email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    username = serializers.CharField(required=False)

    def create(self, validated_data):
        user_data = validated_data['user']
        user = User.objects.create_user(username=user_data['username'],
                                        email=user_data['email'], password=user_data['password'])
        Token.objects.create(user=user)
        return UserProfile.objects.create(user=user, username=user.username)

    class Meta:

        model = UserProfile
        fields = ['user', 'username']


class CourseSerializer(serializers.ModelSerializer):

    average_grade = serializers.SerializerMethodField(method_name='get_average_grade')
    average_workload = serializers.SerializerMethodField(method_name='get_average_workload')
    average_rating = serializers.SerializerMethodField(method_name='get_average_rating')

    def get_average_grade(self, obj):
        avg_dict = Review.objects.filter(course=obj).aggregate(Avg('grade'))
        avg_grade = avg_dict['grade__avg']
        if avg_grade is not None:
            return round(avg_grade)
        return -1


    def get_average_workload(self, obj):
        avg_dict = Review.objects.filter(course=obj).aggregate(Avg('workload'))
        avg_workload = avg_dict['workload__avg']
        if avg_workload is not None:
            return round(avg_dict['workload__avg'])
        return -1

    def get_average_rating(self, obj):
        avg_dict = Review.objects.filter(course=obj).aggregate(Avg('rating'))
        avg_rating = avg_dict['rating__avg']
        if avg_rating is not None:
            return round(avg_rating)
        return -1

    class Meta:
        model = Course
        fields = ('code', 'title', 'description', 'prerequisites',
                  'average_grade', 'average_workload', 'average_rating')


class UpvoteSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        return attrs

    class Meta:
        model = Upvote
        extra_kwargs = {'review': {'required': False}}
        fields = ('author', 'review')


class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    course = serializers.CharField(required=False)
    upvotes = UpvoteSerializer(source='upvote_set', many=True, read_only=True)

    class Meta:
        model = Review
        fields = ['pk', 'author', 'course', 'date_created', 'rating', 'year_taken', 'subclass', 'professor',
                  'assessment', 'grade', 'workload', 'review', 'suggestions', 'upvotes']
