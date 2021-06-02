from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from slugify import slugify

class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Post(models.Model):
    Author=models.ForeignKey(User,on_delete=models.CASCADE)
    Title=models.CharField(max_length=120)
    Content=models.TextField()
    tags=models.ManyToManyField(Tag)
    time_of_publishment=models.DateTimeField(default=timezone.now)
    time_of_modification=models.DateTimeField(auto_now=True,auto_now_add=False)
    thumb = models.ImageField(default='default.jpg',blank=True)

    def __str__(self):
        return self.Title # returns title of the post

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def snippet(self):
        return self.body[:50]

# Comment Section
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete = models.CASCADE)
    author = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

        #to get all the comments approved by superuser
    def get_absolute_url(self):
        return reverse('blog-home')
        #this will return to the main page, all the posts will be displayed on main page.

    def __str__(self):
        return self.text

class Question(models.Model):
    qid=models.AutoField(primary_key=True)
    question_title=models.CharField(max_length=100)
    question_content=models.TextField(max_length=50000)
    date_posted=models.DateTimeField(auto_now_add=True)
    posted_by=models.TextField(max_length=20)
    slug=models.SlugField(max_length=40,null=True)

    class Meta:
        verbose_name = "question"
        ordering = ['date_posted']
    def __str__(self):
        return self.question_title

    def save(self,*args,**kwargs):
        self.slug=slugify(self.question_title)
        super(Question,self).save(*args,**kwargs)

class Answer(models.Model):
    aid=models.AutoField(primary_key=True)
    qid=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_content=models.TextField(max_length=50000)
    date_posted=models.DateTimeField(auto_now_add=True)
    posted_by=models.TextField(max_length=20,default="Anonymous")
