from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def blogView(request,blogauthor,category,blogname):
	content = get_object_or_404(Post,title_slug=blogname)

	context = {
	'content':content,
	}

	return render(request,"post.html",context)
