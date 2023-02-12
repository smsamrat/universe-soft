from django.urls import path,include
from StudentApp.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses', CourseSerializerView, basename='course_id')

urlpatterns = [
    path('courses_view/',include(router.urls)),
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('cdetail/',StudentSerializersView.as_view(), name='course-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]