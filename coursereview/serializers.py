from rest_framework import serializers
from .models import UserProfile, Course, Review, User


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['username', 'email', 'password']


# TODO: user profile info update
class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    def create(self, validated_data):
        user_data = validated_data['user']
        user = User.objects.create_user(username=user_data['username'],
                                        email=user_data['email'], password=user_data['password'])
        return UserProfile.objects.create(user=user, username=user.username)

    class Meta:

        model = UserProfile
        fields = ['user', 'username']


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['code', 'title', 'description', 'prerequisites']


class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    course = serializers.CharField(required=False)

    class Meta:
        model = Review
        fields = ['pk', 'author', 'course', 'date_created', 'rating', 'year_taken', 'subclass', 'professor', 'assessment', 'grade',
                  'workload', 'review', 'suggestions']
