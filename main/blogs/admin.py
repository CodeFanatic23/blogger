from django.contrib import admin
from django.utils.html import format_html
from .models import *
from .forms import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','author','category','date','Status','show_firm_url']
	search_fields = ['title','category']
	list_filter = ['category','status']
	actions = ['preview']
	# model = Post

	def author(self,obj):
		return obj.blogauthor
	def Status(self,obj):
		if obj.status == 'Publish':
			return obj.status + 'ed'
		else:
			return obj.status
	def show_firm_url(self, obj):
		return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.link_to_post)
	
	show_firm_url.short_description = "Link To Post"

	form = PostForm

admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category']

	model = Category

admin.site.register(Category,CategoryAdmin)