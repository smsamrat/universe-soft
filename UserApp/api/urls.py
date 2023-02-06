from django.urls import path
from UserApp.api.views import UserRegistrationView

urlpatterns = [
    path('register_student/',UserRegistrationView.as_view(), name='register_student' )
]