from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desciption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Note(models.Model):
        Course = models.ForeignKey(Course, on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
             return self.title

