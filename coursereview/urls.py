from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views

from . import views

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('token-auth/', authtoken_views.obtain_auth_token),
    path('verify_login/', views.UserLoginVerifier.as_view()),
    path('users/<str:username>/', views.UserProfileDetail.as_view(), name='user'),
    path('users/', views.UserProfileList.as_view(), name='users'),
    path('courses/<str:code>/reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review'),
    path('courses/<str:code>/reviews/', views.ReviewList.as_view(), name='reviews'),
    path('courses/<str:code>/', views.CourseDetail.as_view(), name='course'),
    path('courses/', views.CourseList.as_view(), name='courses')
]
