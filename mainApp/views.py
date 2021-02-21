from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        AllowAny,
                                        BasePermission,
                                        SAFE_METHODS)

from .serializers import *
from .models import Teacher, Video


        #######
        # API #
        #######

class IsProfileOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == view.get_object()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user



class TeacherProfileView(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    
    queryset = Teacher.objects.all()
    serializer_class = TeacherProfileSerializer


   
class DetailTeacherProfileView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]

    queryset = Teacher.objects.all()
    serializer_class = TeacherProfileSerializer



class StudentProfileView(generics.ListAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer
    
    

class DetailStudentProfileView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]

    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer



class IsTeacherOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return isinstance(view.get_object().user, Teacher)



class CourseView(generics.ListCreateAPIView):
    
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class IsCourseOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == view.get_object().teacher


class DetailCourseView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly, IsCourseOwnerOrReadOnly]
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class ArticleView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class DetailArticleView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class VideoView(generics.ListCreateAPIView):
    
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



class CourseVideoView(generics.ListAPIView):

    serializer_class = [IsAuthenticated]
    serializer_class = VideoSerializer

    def get_queryset(self):
        queryset = Video.objects.all()
        course_id = self.kwargs.get('pk')
        if course_id is not None:
            return queryset.filter(course=course_id)
        return None



class DetailVideoView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



class CommentView(generics.ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class DetailCommentView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class ReplyView(generics.ListCreateAPIView):
    
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer



class DetailReplyView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
