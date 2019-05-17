from django.db import models

# Create your models here.
from api.courses.models import Courses
from api.users.models import User


class Lessons(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=124, null=False)
    description = models.TextField(null=True)
    score = models.FloatField(null=False)
    lesson_previous = models.ForeignKey('Lessons', null=True, blank=True, related_name='previous', on_delete=models.SET_NULL)
    lesson_next = models.ForeignKey('Lessons', null=True, blank=True, related_name='next', on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        try:
            if self.id is None:
                previous_lesson = Lessons.objects.get(lesson_next=None)
                self.lesson_previous = previous_lesson
                super(Lessons, self).save(*args, **kwargs)
                previous_lesson.lesson_next = self
                previous_lesson.save()
            else:
                super(Lessons, self).save(*args, **kwargs)
        except:
            super(Lessons, self).save(*args, **kwargs)

    def delete(self):
        try:
            lesson = Lessons.objects.get(pk=self.lesson_previous.pk)
            lesson.next_lesson = self.next_lesson
            lesson.save()
        except:
            pass
        try:
            lesson = Lessons.objects.get(pk=self.next_lesson.pk)
            lesson.lesson_previous = self.lesson_previous
            lesson.save()
        except:
            pass
        super(Lessons, self).delete()


