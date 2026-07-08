from django.db import models
from django.contrib.auth.models import User

TAG_CHOICES = [
    ('exam', 'امتحان'),
    ('exercise', 'تمرین'),
    ('project', 'پروژه'),
    ('lecture', 'جزوه'),
]

PRICE_CHOICES = [
    ('free', 'رایگان'),
    ('paid', 'پولی'),
]


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Note(models.Model):
        course = models.ForeignKey(Course, on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        content = models.TextField(blank=True, null=True)
        file = models.FileField(upload_to='notes/files/', blank=True, null=True)
        tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='lecture')
        is_public = models.BooleanField(default=False)
        price_type = models.CharField(max_length=10, choices=PRICE_CHOICES, default='free')
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
             return self.title


class Rating(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('note', 'user')



class Comment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.text[:20]}'