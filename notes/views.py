from django.shortcuts import render , get_object_or_404, redirect
from .models import Course, Note
from .forms import RegisterForm
from django.contrib.auth import login as auth_login


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'notes/course_list.html', {'courses': courses})

def note_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    notes = course.note_set.all()
    return render(request, 'notes/note_list.html', {'course':course, 'notes': notes})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('course_list')
    
    else:
        form = RegisterForm()
    return render(request, 'notes/register.html', {'form': form})
