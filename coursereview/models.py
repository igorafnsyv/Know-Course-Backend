from django.db import models

# Create your models here.


class Course(models.Model):
    code = models.CharField(max_length=8, primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # course may have many pre-requisites.  Course may be pre-requisite to many courses
    prerequisites = models.ManyToManyField('Course', blank=True)

    def __str__(self):
        return self.code


class Review(models.Model):
    course = models.ForeignKey('Course', null=False, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    # Allows students to rate whether review was helpful. Thumbs up -> +1, down -> -1
    rating = models.IntegerField(default=0)
    year_taken = models.IntegerField(null=False)
    # Subclass A, B or C
    subclass = models.CharField(max_length=1)
    professor = models.CharField(max_length=50, null=False)
    assessment = models.CharField(max_length=50)
    # A+,A,A-...
    grade = models.CharField(max_length=2)
    # workload - hell, high, average, low, super easy
    # add user - author of comment
    review = models.TextField()
    # suggestion for people who will be taking the course in the future
    suggestions = models.TextField()




