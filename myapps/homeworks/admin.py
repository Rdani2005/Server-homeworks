from django.contrib import admin
from .models import Subject, Homework, FilesHomework, ImageHomeworks

class ImageHomeworksAdmin(admin.TabularInline):
    model = ImageHomeworks

class FilesHomeworkAdmin(admin.TabularInline):
    model = FilesHomework


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

# Admin view using Homework model
@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'description', 'slug', 'created', 'updated']
    list_filter = ['is_delivered']
    list_editable = []
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ImageHomeworksAdmin,
        FilesHomeworkAdmin,
    ]

