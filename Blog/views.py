from django.shortcuts import render, redirect
from jdatetime import date
from Blog.models import Comment, Post

from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages


#post form with model's form
def home_view(request):
    template_name = 'Blog/home.html'
    context = {}
    return render(request, template_name, context)


# post's form)
def post_view(request):
    template_name = 'Blog/post.html'
    context = {}
    context['posts_count'] = Post.objects.all().count()
    context['published_posts'] = Post.objects.filter(state = 1)
    return render(request, template_name, context)


#detail_post's form
def post_detail_view(request,slug):
    template_name = 'Blog/detail.html'
    context = {}
    post_detail = Post.objects.get(slug=slug)
    comments = post_detail.comments.filter(state = 1)
    context['post_detail'] = post_detail
    context['comments'] = comments
    return render(request, template_name, context)