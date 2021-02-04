from rest_framework import serializers
from .models import *


class TeacherProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('avatar', 'bio', 'date_created') 



class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('avatar', 'bio', 'date_created') 



class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'



class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'



class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'



class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = '__all__'

