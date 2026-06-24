from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Course, Note
from .forms import RegisterForm, CourseForm, NoteForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'notes/course_list.html', {'courses': courses})

def note_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    notes = course.note_set.all() # ✅ اصلاح شد
    return render(request, 'notes/note_list.html', {'course': course, 'notes': notes})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('course_list')
    else:
        form = RegisterForm()
    return render(request, 'notes/register.html', {'form': form})

@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'notes/course_form.html', {'form': form})

@login_required
def note_create(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.course = course
            note.save()
            return redirect('note_list', course_id=course.id)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'course': course})

