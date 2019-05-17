from django.db import models

# Create your models here.
from api.users.models import User


class Courses(models.Model):
    title = models.CharField(max_length=124, null=False)
    description = models.TextField(null=True)
    course_previous = models.ForeignKey('Courses', null=True, blank=True, related_name='previous', on_delete=models.SET_NULL)
    course_next = models.ForeignKey('Courses', null=True, blank=True, related_name='next', on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        try:
            if self.id is None:
                previous_course = Courses.objects.get(course_next=None)
                self.course_previous = previous_course
                super(Courses, self).save(*args, **kwargs)
                previous_course.course_next = self
                previous_course.save()
            else:
                super(Courses, self).save(*args, **kwargs)
        except:
            super(Courses, self).save(*args, **kwargs)

    def delete(self):
        try:
            course = Courses.objects.get(pk=self.course_previous.pk)
            course.course_next = self.course_next
            course.save()
        except:
            pass
        try:
            course = Courses.objects.get(pk=self.course_next.pk)
            course.course_previous = self.course_previous
            course.save()
        except:
            pass
        super(Courses, self).delete()



