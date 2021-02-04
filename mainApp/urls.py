from django.urls import path
from .views import *



urlpatterns = [
    path('teacher/',          TeacherProfileView.as_view()),
    path('teacher/<int:pk>/', DetailTeacherProfileView.as_view()),
    path('student/',          StudentProfileView.as_view()),
    path('student/<int:id>/', DetailStudentProfileView.as_view()),
    path('course/',           CourseView.as_view()),
    path('article/',          ArticleView.as_view()),
    path('video/',            VideoView.as_view()),
    path('comment/',          CommentView.as_view()),
    path('reply/',            ReplyView.as_view()),
] 
