
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('UserApp.urls')),
    path('', include('StudentApp.urls')),
    path('studentapi/', include('StudentApp.api.urls')),
]
