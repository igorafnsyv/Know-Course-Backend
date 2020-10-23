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

