from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Course, Note
from .forms import RegisterForm, CourseForm, NoteForm
from django.db.models import Q
from django.contrib.auth.models import User


@login_required
def course_list(request):
    courses = Course.objects.filter(user=request.user)
    public_users = User.objects.filter(course__note__is_public=True).distinct()
    return render(request, 'notes/course_list.html', {'courses': courses, 'public_users':public_users})

def note_list(request, course_id):
    course = get_object_or_404(Course, id=course_id, user=request.user)
    tag = request.GET.get('tag')
    if tag:
        notes = course.note_set.filter(tag=tag)
    else:
        notes = course.note_set.all()
    return render(request, 'notes/note_list.html', {'course': course, 'notes': notes, 'selected_tag': tag})

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
def course_delete(request, course_id):
    try:
        course = get_object_or_404(Course,id=course_id, user=request.user)
        course.delete()
    except Course.DoesNotExist:
        pass
    return redirect('course_list')

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


@login_required
def note_delete(request, note_id):
    try:
        note = get_object_or_404(Note, id=note_id)
        course_id =note.course.id
        if note.course.user == request.user:
            note.delete()
        return redirect('note_list', course_id=course_id)
    except Note.DoesNotExist:
        return redirect('course_list')
    

@login_required
def search_notes(request, course_id):
    course = get_object_or_404(Course, id=course_id,user=request.user)
    query = request.GET.get('q')
    if query:
        notes = course.note_set.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    else:
        notes = Note.objects.none()
    return render(request, 'notes/search_results.html', {'notes': notes, 'query':query})

@login_required
def search_courses(request):
    query = request.GET.get('q','').strip()
    if query:
        courses = Course.objects.filter(
            user=request.user,
            name__icontains=query
        )
    else:
        courses = Course.objects.none()
    return render(request, 'notes/search_courses.html', {'courses': courses, 'query': query})


@login_required
def dashboard(request):
    user = request.user
    courses = Course.objects.filter(user=user)
    total_courses = courses.count()
    total_notes = Note.objects.filter(course__user=user).count()
    recent_notes = Note.objects.filter(course__user=user).order_by('-created_at')[:5]

    context = {
        'user': user,
        'total_courses': total_courses,
        'total_notes': total_notes,
        'recent_notes': recent_notes,
    }
    return render(request, 'notes/dashboard.html', context)



def public_profile(request, username):
    user = get_object_or_404(User, username=username)
    notes = Note.objects.filter(course__user=user, is_public=True)
    context = {
        'profile_user': user,
        'notes': notes,
    }
    return render(request, 'notes/public_profile.html', context)


def public_notes_list(request):
    tag = request.GET.get('tag')
    query = request.GET.get('q')
    notes = Note.objects.filter(is_public=True)
    if tag:
        notes = notes.filter(tag=tag)
    if query:
        notes = notes.filter(
            Q(title__icontains=query) |
            Q(course__name__icontains=query)
        )
    return render(request, 'notes/public_notes_list.html', {'notes': notes})


def public_note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.course = get_object_or_404(Course, id=request.POST.get('course'))
            note.save()
            return redirect('public_profile', username=request.user.username)
    else:
        form = NoteForm()
    courses = Course.objects.filter(user=request.user)
    return render(request, 'notes/public_note_create.html', {'form': form, 'courses': courses})