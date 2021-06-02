from django.contrib import admin
from .models import Post, Comment, Question, Answer, Tag
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Answer)
