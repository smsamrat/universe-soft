from django.urls import path
from StudentApp.api.views import *
urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register')
]