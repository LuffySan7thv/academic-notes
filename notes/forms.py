from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Course,Note
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("نام کاربری تکراری است. لطفا نام کاربری دیگری انتخاب کنید❌❗")
        return username
    
    def clean_password1(self):
        self.password1 = self.cleaned_data.get('password1')
        if len(self.password1)< 8:
            raise forms.ValidationError("رمزعبور باید حداقل8 کارکتر باشد❗❌")
        return self.password1

class CustomLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError("این کاربر غیر فعال است")


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'file', 'tag','is_public']
