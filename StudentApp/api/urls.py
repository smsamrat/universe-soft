from django.urls import path
from StudentApp.api.views import *
urlpatterns = [
    path('register/',StudentRecordView.as_view(), name='register')
]