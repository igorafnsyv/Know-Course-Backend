from rest_framework import serializers
from .models import UserProfile, Course, Review, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop('user')
        usr = User.objects.create_user(username=user_data.pop('username'),
                                       email=user_data.pop('email'), password=user_data.pop('password'))
        return UserProfile.objects.create(user=usr, username=usr.username)

    class Meta:

        model = UserProfile
        fields = ['user', 'username']


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
        fields = ['author', 'course', 'date_created', 'rating', 'year_taken', 'subclass', 'professor', 'assessment', 'grade',
                  'review', 'suggestions']