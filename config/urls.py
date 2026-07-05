from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from notes.forms import CustomLoginForm
from django.conf import settings
from django.conf.urls.static import static
from notes.views import (
    course_list, note_list, register, note_create, course_create,
    course_delete, note_delete, search_notes,search_courses,dashboard,public_profile,
    public_notes_list,public_note_create
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', course_list, name='course_list'),
    path('course/<int:course_id>/', note_list, name='note_list'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(
        template_name='notes/login.html',
        redirect_authenticated_user=True,
        next_page='/'
    ), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('course/<int:course_id>/note/create/', note_create, name='note_create'),
    path('course/create/', course_create, name='course_create'),
    path('course/<int:course_id>/delete/', course_delete, name='course_delete'),
    path('note/<int:note_id>/delete/', note_delete, name='note_delete'),
    path('search/courses/', search_courses, name='search_courses'),
    path('search/notes/<int:course_id>/',search_notes, name='search_notes'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/<str:username>/', public_profile, name='public_profile'),
    path('public/notes/', public_notes_list, name='public_notes_list'),
    path('public/note/create/', public_note_create, name='public_note_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

