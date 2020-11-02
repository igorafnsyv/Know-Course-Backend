from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.username


class Course(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # course may have many pre-requisites.  Course may be pre-requisite to many courses
    prerequisites = models.ManyToManyField('Course', blank=True)

    def __str__(self):
        return self.code


class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    # Allows students to rate whether review was helpful. Thumbs up -> +1, down -> -1
    rating = models.IntegerField(default=0)
    year_taken = models.IntegerField(null=False)
    # Subclass A, B or C
    subclass = models.CharField(max_length=1, blank=True)
    professor = models.CharField(max_length=50)
    assessment = models.CharField(max_length=50)
    # A+,A,A-...
    grade = models.CharField(max_length=2)
    # Workload info -> the higher the more workload there is
    workload = models.IntegerField(default=0)
    review = models.TextField()
    # suggestion for people who will be taking the course in the future
    suggestions = models.TextField(blank=True)




