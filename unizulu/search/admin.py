from django.contrib import admin

# Register your models here.
from . models import Courses, degree

admin.site.register(Courses)
admin.site.register(degree)

#class AuthorAdmin(admin.ModelAdmin):
#list_display = ('course_name','faculty','points_requirements','subject_requirements','careers_offered')

