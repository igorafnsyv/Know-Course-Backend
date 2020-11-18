from django.contrib import admin

from coursereview.models import *

admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Review)

# Register your models here.
