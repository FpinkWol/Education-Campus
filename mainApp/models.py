'''
Models:
    Teacher
    Student
    Course
    Article
    Video
    Comment
    Reply
    VideoView
    VideoLike
    ArticleView
    ArticleLike
'''
from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User


CATEGORY=[
    ('PRG', 'Programming'),
    ('UNI', 'University')
]


class AbstractProfile(models.Model):

    avatar = models.ImageField(upload_to='static/avatar/', blank=True)
    bio = models.CharField(max_length=270, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Teacher(User, AbstractProfile):
    
    class Meta:
        verbose_name="Teacher"

    def __str__(self):
        return self.username



class Student(User, AbstractProfile):

    class Meta:
        verbose_name="Student"

    def __str__(self):
        return self.username



class Course(models.Model):

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 
    category = models.CharField(max_length=100, choices=CATEGORY)
    context = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created',]
   
    def __str__(self):
        return f'{self.context} -- {self.teacher.username}'



class Article(models.Model):
    
    author = models.ForeignKey(Teacher, related_name='teacher_article', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_created',]
   
    def __str__(self):
        return f'{self.title} -- {self.author.username}'

    

class Video(models.Model):

    subject = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='static/video/')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.course.teacher.username} : {self.course.context}'

    def get_absolute_url(self):
        return f'/{self.course.context}/{self.subject}/'


# usage: teacher can't comment on her/his video
def can_comment(user, video):
    return video.course.teacher is user



class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=270)
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:30]



class Reply(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.CharField(max_length=270)
    comment = models.ForeignKey(Comment, related_name='replys', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.reply[:30]



class VideoView(models.Model):

    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('video', 'user'),) 



class VideoLike(models.Model):
    
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('video', 'user'),) 
 


class ArticleView(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('article', 'user'),) 



class ArticleLike(models.Model):
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('article', 'user'),) 
