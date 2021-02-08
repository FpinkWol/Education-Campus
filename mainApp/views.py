from django.http import HttpResponse, JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

from .serializers import *
from .models import Teacher, Video


        #######
        # API #
        #######

class TeacherProfileView(generics.ListAPIView):
    
    queryset = Teacher.objects.all()
    serializer_class = TeacherProfileSerializer


   
class DetailTeacherProfileView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Teacher.objects.all()
    serializer_class = TeacherProfileSerializer



class StudentProfileView(generics.ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer
    
    

class DetailStudentProfileView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer



class CourseView(generics.ListCreateAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class DetailCourseView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class ArticleView(generics.ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class DetailArticleView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class VideoView(generics.ListCreateAPIView):
    
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



class CourseVideoView(generics.ListAPIView):

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
