from django.urls import path
from .views import CoursesView, CoursesListView

urlpatterns = [
    path('courses/', CoursesListView.as_view()),
    path('courses/<int:id>', CoursesView.as_view()),
]