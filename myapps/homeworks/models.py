# Django: http://docs.djangoproject.com/
from django.db import models # used for create DB Models
from django.urls import reverse # 


class HomeworkManager(models.Manager):
    def get_queryset(self):
        return super(HomeworkManager, self).get_queryset().filter(is_delivered=True)

"""
    Model to define the subject of the homework that we are working on
"""
class Subject(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Subjects"
    
    def get_absolute_url(self):
        return reverse('project:subject_list', args=[self.slug])

    def __str__(self):
        return self.title

class Homework(models.Model):
    subject = models.ForeignKey(Subject, related_name='homework', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_delivered = models.BooleanField(default=True)
    objects = models.Manager()
    homeworks = HomeworkManager()

    # Extra instructions
    class Meta:
        verbose_name_plural = 'Homeworks'
        ordering = ('-created',)

    #Return the URL
    def get_absolute_url(self):
        return reverse('homeworks:homework_detail', args=[self.slug])
    # Return the title of the project, in case of needing it
    def __str__(self):
        return self.title

class FilesHomework(models.Model):
    file = models.FileField(upload_to='docs/homework-files/%Y-%m-%d')
    homework = models.ForeignKey(Homework, related_name='files_homework', on_delete=models.CASCADE)

class ImageHomeworks(models.Model):
    image = models.ImageField(upload_to='images/uploaded/%Y-%m-%d')
    homework = models.ForeignKey(Homework, related_name='image_homeworks', on_delete=models.CASCADE)