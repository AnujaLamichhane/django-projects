from django.urls import path
from . import views

urlpatterns = [
    path('',views.workshop_list,name='workshop_list'),
    # path('workshops/', views.workshop_list, name='workshop_list'),
    path("detail/<int:id>", views.workshop_detail, name="workshop_detail"),
    # path('members/', views.member_list, name='member_list'),
    # path('members/<int:member_id>/', views.member_detail, name='member_detail'),
]
