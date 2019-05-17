from django.urls import path
from .views import LessonsListView, LessonsView

urlpatterns = [
    path('lessons/', LessonsListView.as_view()),
    path('lessons/<int:id>', LessonsView.as_view()),
]