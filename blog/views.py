from django.shortcuts import render, redirect
from .models import Post, Comment, Contact, Category
from .forms import CommentForm, ContactForm, CreatePostForm
from django.contrib import messages   


def home(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'blog/home.html', {"posts": posts, "title": "Blog Page"})


def category_blog(request):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    return render(request, 'blog/category_blog.html', {"category": category, "posts": posts})



def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            body = form.cleaned_data.get('body')

            comment = Comment(author=author, body=body, post=post)
            comment.save()

    comments = Comment.objects.filter(post=post)
    return render(request, 'blog/blog_detail.html', {"post": post, "comments": comments, "form": form})



def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')  
            form.save()
            messages.success(request, f'Votre message a été envoyé avec succès !')
            return redirect('contact-form')
    else:
        form = ContactForm()
    return render(request, 'blog/contact_form.html', {"form": form, "title": "Contact | Form"})


def about(request):
    return render(request, 'blog/about.html', {"title": "About"})



def createPost(request):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    if request.method=='POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            body = form.cleaned_data.get('body')
            post = Post(title=title, body=body, posts=posts)
            post.save()
            messages.success(request, f'Votre article a été envoyé avec succès !')
            return redirect('create-post')
    else:
        form = CreatePostForm()
    return render(request, 'blog/create_post.html', {'form': form, "post": post})