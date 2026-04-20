from django.shortcuts import redirect, render
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
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blogapp/signup.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been created!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blogapp/create_post.html', {'form': form})  
 
def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'blogapp/post_detail.html', {'post': post})
