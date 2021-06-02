from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import AnswerForm, AnonymousCommentForm
from .models import Tag, Post
from users.models import Profile
from django.core.paginator import Paginator
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
        )
from .models import Post, Comment
from .models import Question
from .models import Answer
from django.http import HttpResponse
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(Title__icontains=query)).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'blog/search_results.html', context)



def get_tag_count():
    queryset = Post.objects.values('tags__title').annotate(Count('tags__title'))

    return queryset

def question(request):
    form = AnswerForm(request.POST or None, request.FILES)
    questions=Question.objects.all()
    tags = Tag.objects.all()
    for question in questions :
        question.answer = question.answer_set.all()
    return render(request, 'blog/question.html',{'questions': questions,'tags':tags,'form':form})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-time_of_publishment']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

def get_query_set(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    tag_count = get_tag_count()

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['Title','Content', 'thumb', 'tags']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['Title','Content', 'thumb', 'tags']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title':'about','tags' : Tag.objects.all()})

def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
        context = {
        'post' : post,
        'is_liked' : is_liked,
        'total_likes' : post.total_likes(),
        'tags' : Tag.objects.all(),
        }
        return render(request, 'blog/post_detail.html', context)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    username = request.user.username
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = username
            comment.save()
            return redirect('post-detail', pk=post.id)#avant pk = post.pk
    else:
        form = CommentForm
    return render(request,'blog/comment_form.html',{'form': form})

@login_required
def comment_approve(request,pk) :
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-detail', pk = comment.post.pk)

@login_required
def comment_remove(request,pk) :
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post-detail', pk = post_pk)

def add_anonymous_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = AnonymousCommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data["author"]
            comment = form.save(commit=False)
            comment.post = post
            comment.author = "Anonymous-"+author
            comment.approved_comment = False
            comment.save()
            return redirect('post-detail', pk=post.id)#avant pk = post.pk
    else:
        form = AnonymousCommentForm
    return render(request,'blog/comment_form.html',{'form': form})


#Answers
def new_answer(request):
    sauvegarde = False
    questions=Question.objects.all()
    for question in questions :
        question.answer = question.answer_set.all()
    form = AnswerForm(request.POST or None, request.FILES)
    if form.is_valid():
        answer_content = form.cleaned_data["answer_content"]
        qid = request.POST.get('qid', None)
        question = get_object_or_404(Question,qid=qid)
        answer = Answer()
        answer.answer_content=answer_content
        answer.posted_by = request.user.username
        answer.qid=question
        answer.save()
        sauvegarde = True
        form = AnswerForm()
    return render(request, 'blog/question.html', {
        'form': form,
        'sauvegarde': sauvegarde,
        'questions': questions
    })
##Homepage
def home(request):
    posts =Post.objects.all().order_by('-time_of_publishment')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts,
        'tags' : Tag.objects.all(),
        'newprofiles' : Profile.objects.filter(approved_user="False"),
        'pending_rolesprofiles' : Profile.objects.filter(change_role="True")
    }
    return render(request, 'blog/home.html',context)
#sorting from newest to oldest
def newest(request):
    posts =Post.objects.all().order_by('-time_of_publishment')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts,
        'tags' : Tag.objects.all(),
        'newprofiles' : Profile.objects.filter(approved_user="False"),
        'pending_rolesprofiles' : Profile.objects.filter(change_role="True")
    }
    return render(request, 'blog/home.html',context)
#sorting from oldest to newest
def oldest(request):
    posts =Post.objects.all().order_by('time_of_publishment')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts,
        'tags' : Tag.objects.all(),
        'newprofiles' : Profile.objects.filter(approved_user="False"),
        'pending_rolesprofiles' : Profile.objects.filter(change_role="True")
    }
    return render(request, 'blog/home.html',context)

def get_posts_by_tag(request,title):
    tag = get_object_or_404(Tag, title=title)
    postsTag = tag.post_set.all()
    tags = Tag.objects.all()
    return render(request, 'blog/home.html', {'posts': postsTag,'tags':tags})

def displayPost(request,pk):
    post = Post.objects.get(id=pk)
    tags = Tag.objects.all()
    form = CommentForm
    anonym_form = AnonymousCommentForm
    return render(request, 'blog/post_detail.html', {'post': post,'tags':tags,'form':form,'anonym_form':anonym_form})

def list_myPosts(request,id_user):
    user = get_object_or_404(User, id=id_user)
    myPosts = user.post_set.all()
    context = {
        'posts': myPosts,
        'tags' : Tag.objects.all()
    }
    return render(request, 'blog/home.html',context)


def contact(request):
    return render(request, 'blog/contactus.html', {'title':'contact'})
###Profile managers
@login_required
def profile_approve(request,pk) :
    profile = get_object_or_404(Profile, pk=pk)
    profile.approve()
    context = {
        'posts': Post.objects.all(),
        'tags' : Tag.objects.all(),
        'newprofiles' : Profile.objects.filter(approved_user="False"),
        'pending_rolesprofiles' : Profile.objects.filter(change_role="True")
    }
    return render(request, 'blog/home.html',context)

@login_required
def profile_remove(request,pk) :
    profile = get_object_or_404(Profile, pk=pk)
    profile.delete()
    context = {
        'posts': Post.objects.all(),
        'tags' : Tag.objects.all(),
        'newprofiles' : Profile.objects.filter(approved_user="False"),
        'pending_rolesprofiles' : Profile.objects.filter(change_role="True")

    }
    return render(request, 'blog/home.html',context)

## Roles Managers :
@login_required
def role_approve(request,pk) :
    profile = get_object_or_404(Profile, pk=pk)
    profile.changeRole()
    context = {
        'posts': Post.objects.all(),
        'tags' : Tag.objects.all(),
        'newprofiles' : Profile.objects.filter(approved_user="False"),
        'pending_rolesprofiles' : Profile.objects.filter(change_role="True")
    }
    return render(request, 'blog/home.html',context)

@login_required
def role_remove(request,pk) :
    profile = get_object_or_404(Profile, pk=pk)
    profile.change_role = False
    profile.new_type= 'Anonymous'
    profile.save()
    context = {
        'posts': Post.objects.all(),
        'tags' : Tag.objects.all(),
        'newprofiles' : Profile.objects.filter(approved_user="False"),
        'pending_rolesprofiles' : Profile.objects.filter(change_role="True")

    }
    return render(request, 'blog/home.html',context)
