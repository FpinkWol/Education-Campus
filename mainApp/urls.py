from django.urls import path
from .views import *



urlpatterns = [
    path('teacher/',          TeacherProfileView.as_view()),
    path('teacher/<int:pk>/', DetailTeacherProfileView.as_view()),
    path('student/',          StudentProfileView.as_view()),
    path('student/<int:pk>/', DetailStudentProfileView.as_view()),
    path('course/',           CourseView.as_view()),
    path('course/<int:pk>/',  DetailCourseView.as_view()),
    path('course/<int:pk>/video/',     CourseVideo.as_view()),
    path('article/',          ArticleView.as_view()),
    path('article/<int:pk>/', DetailArticleView.as_view()),
    path('video/',            VideoView.as_view()),
    path('video/<int:pk>/',   DetailVideoView.as_view()),
    path('comment/',          CommentView.as_view()),
    path('comment/<int:pk>/', DetailCommentView.as_view()),
    path('reply/',            ReplyView.as_view()),
    path('reply/<int:pk>/',   DetailReplyView.as_view()),
] 
