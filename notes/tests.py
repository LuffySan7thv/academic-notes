from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, Note

#تست مدل‌ها
class ModelTests(TestCase):
    def test_create_course(self):
        user = User.objects.create_user(username='testuser', password='12345')
        course = Course.objects.create(user=user, name='ریاضی')
        self.assertEqual(course.name, 'ریاضی')
        self.assertEqual(course.user.username, 'testuser')

    def test_create_note(self):
        user = User.objects.create_user(username='testuser', password='12345')
        course = Course.objects.create(user=user, name='ریاضی')
        note = Note.objects.create(course=course, title='جزوه ۱', content='محتوا')
        self.assertEqual(note.title, 'جزوه ۱')
        self.assertEqual(note.course.name, 'ریاضی')

#تست ویوها
class ViewTests(TestCase):
    def setUp(self):
        # این کاربر یک بار قبل از همه‌ی تست‌ها ساخته میشه
        self.user = User.objects.create_user(username='test', password='123')

    def test_course_list_redirect_if_not_logged_in(self):
        # لاگین نیست باید به لاگین بره کد 302
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_course_list_view_with_login(self):
        # لاگین میکنیم
        self.client.login(username='test', password='123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/course_list.html')


def test_register_view(self):
    response = self.client.post('/register/', {
        'username': 'newuser',
        'password1': 'testpass123',
        'password2': 'testpass123'
    })
    self.assertEqual(response.status_code, 302) # بعد از ثبت‌نام ریدایرکت میشه

def test_create_course_view(self):
    self.client.login(username='test', password='123')
    response = self.client.post('/course/create/', {'name': 'فیزیک'})
    self.assertEqual(response.status_code, 302) # ریدایرکت به لیست درس‌ها


def test_note_list_view(self):
    self.client.login(username='test', password='123')
    course = Course.objects.create(user=self.user, name='ریاضی')
    response = self.client.get(f'/course/{course.id}/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'notes/note_list.html')


