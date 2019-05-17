import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
#from api.courses.models import Courses
#from api.lessons.models import Lessons


class User(AbstractUser):
    activation_token = models.UUIDField(default=uuid.uuid4)

#class UserLessons(models.Model):
#
#    user = models.ForeignKey(User, on_delete=models.SET_NULL)
#    lessons = models.ForeignKey(Lessons, on_delete=models.SET_NULL, related_name='lessons')
#    courses = models.ForeignKey(Courses, on_delete=models.SET_NULL)
#    score = models.ForeignKey(Lessons, on_delete=models.SET_NULL, related_name='score')
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)
