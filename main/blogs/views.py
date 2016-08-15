from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


# Create your views here.
def blogView(request,blogauthor,category,blogname):
	content = get_object_or_404(Post,title_slug=blogname)
	print(content.blogauthor)
	context = {
	'data':content,
	}

	return render(request,"post.html",context)

def blogHome(request):
	return HttpResponse("<h1>YOLO!</h1>")
	#return render(request,"post.html",context)

def authorHome(request,blogauthor):
	content_featured = Post.objects.filter(blogauthor_slug=blogauthor,featured=True).order_by('-date')
	content_regular = Post.objects.filter(blogauthor_slug=blogauthor,featured=False).order_by('-date')
	latest =Post.objects.filter(blogauthor_slug=blogauthor,featured=False).latest('date')
	print(content_regular)
	paginator = Paginator(content_regular,1)

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	context ={
	'posts':posts,
	'dataf':content_featured,
	'latest':latest
	}
	
	return render(request,"author.html",context)

def category(request,blogauthor,category):
	content_featured = Post.objects.filter(category__category__iexact=category,featured=True).order_by('-date')
	content_regular = Post.objects.filter(category__category__iexact=category,featured=False).order_by('-date')
	latest =Post.objects.filter(category__category__iexact=category,featured=False).latest('date')
	print(content_regular)
	paginator = Paginator(content_regular,1)

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	context ={
	'posts':posts,
	'dataf':content_featured,
	'latest':latest
	}
	
	
	return render(request,"category.html",context)
