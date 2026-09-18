from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'students/<str:message>/',
        views.student_list,
        name='student_list'
    ),

]