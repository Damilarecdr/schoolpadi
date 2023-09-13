# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')[:10]
    #posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})



def all_posts(request):
    # Retrieve all blog posts
    posts = Post.objects.all()
    return render(request, 'blog/all.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    
    return render(request, 'blog/details.html', {'post': post, 'comments': comments, 'form': form})
# blog/views.py
from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(categories=category)
    return render(request, 'blog/category_detail.html', {'category': category, 'posts': posts})
