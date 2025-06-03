from django.urls import path
# from . import views
from .views import student_api
from .views import department_api

urlpatterns = [
    # path("",views.index, name="index"),
    path('students/api/', student_api, name='student_api'),
    path('department/api/', department_api, name='department_api'),
]
