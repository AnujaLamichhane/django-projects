from django.contrib import admin
from . models import Student
from . models import Department

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
admin.site.register(Student)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'noofstudents')


admin.site.register(Department)

# Register your models here.
