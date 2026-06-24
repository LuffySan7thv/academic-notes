"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from notes.views import course_list, note_list, register,note_create,course_create
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',course_list,name='course_list'),
    path('course/<int:course_id>/', note_list, name='note_list'),
    path('register/', register, name='register'),
    path('login/',LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('course/<int:course_id>/note/create/', note_create,name='note_create'),
    path('course/create/',course_create, name='course_create')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
