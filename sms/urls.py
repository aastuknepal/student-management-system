"""
URL configuration for sms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import    TemplateView
from rest_framework.routers import DefaultRouter
from teacher.views import TeacherSerializer, TeacherViewset
from student.views import StudentSerializer, StudentViewset
from course.views import CourseSerializer, CourseViewset
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    
)
from .views import RegisterView








router = DefaultRouter()


router.register(r'teachers', TeacherViewset, basename='teacher')
router.register(r'students', StudentViewset, basename='student')
router.register(r'courses', CourseViewset, basename='course')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('student.urls')),



    #Global Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', RegisterView.as_view(), name='register'),


    #frontend Template Routes

    path('add-teacher/', TemplateView.as_view(template_name='add_teacher.html'), name='add_teacher'),

    # 1. This generates the raw JSON blueprint of your API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # 2. Swagger UI: The interactive, playable documentation
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # 3. Redoc: A cleaner, read-only version of the documentation
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]

