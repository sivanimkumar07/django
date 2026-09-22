from django.urls import path
from . import views

urlpatterns = [

    path(
        'signup/',
        views.signup_page,
        name='signup'
    ),

    path(
        'login/',
        views.login_page,
        name='login'
    ),

    path(
        'counter/',
        views.counter_page,
        name='counter'
    ),

    path(
        'logout/',
        views.logout_page,
        name='logout'
    ),

]