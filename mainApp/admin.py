from django.contrib import admin 
from .models import (
        Teacher,
        Student,
        Course,
        Article,
        Video,
        Comment,
        Reply)


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Article)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Reply)
