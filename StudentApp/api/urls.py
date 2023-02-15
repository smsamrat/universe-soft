from django.urls import path,include
from StudentApp.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses', CourseSerializerView, basename='course_id'),
router.register('student_pro', StudentProfileView, basename='student_pro')

urlpatterns = [
    path('api/',include(router.urls)),
    
    # add_student login system
    path('student_register/',StudentRegistrationView.as_view(), name='student_register'),
    path('student_register/<int:id>/',StudentRegistrationView.as_view(), name='student_update'),
    
    #User Login
    path('login/',UserLogin.as_view(), name='login'),
    
    # teacher_student login system
    path('teacher_register/',TeacherRegistrationView.as_view(), name='teacher_register'),
    path('teacher_register/<int:id>/',TeacherRegistrationView.as_view(), name='teacher_update'),

    
    
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]