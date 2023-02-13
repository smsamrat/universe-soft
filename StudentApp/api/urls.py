from django.urls import path,include
from StudentApp.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('courses', CourseSerializerView, basename='course_id'),
router.register('student_pro', StudentProfileView, basename='student_pro')

urlpatterns = [
    path('f/',include(router.urls)),
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('register/<int:id>/',UserRegistrationView.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]