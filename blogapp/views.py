from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, UserRegisterForm
from django.contrib import messages


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            posts = Post.objects.all().order_by('-created_at')
        else:
            posts = Post.objects.filter(author=request.user).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blogapp/home.html', {'posts': posts})
def signup(request):
    pass
def create_post(request):
    pass    
def post_detail(request):
    pass
