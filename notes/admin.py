from django.contrib import admin
from .models import Course, Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_at', 'file')


admin.site.register(Course)
admin.site.register(Note, NoteAdmin)
