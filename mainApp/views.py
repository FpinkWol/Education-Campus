from rest_framework import generics
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



class CourseView(generics.ListAPIView,
                 generics.RetrieveUpdateDestroyAPIView): 
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class ArticleView(generics.ListAPIView,
                  generics.RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class VideoView(generics.ListAPIView,
                generics.RetrieveUpdateDestroyAPIView): 
    
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



class CommentView(generics.ListAPIView,
                  generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class ReplyView(generics.ListAPIView,
                generics.RetrieveUpdateDestroyAPIView): 
    
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
