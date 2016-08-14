from django.db import models
from django.conf import settings
from django.db.models import signals
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.sites.models import Site
from datetime import datetime
from django.template.defaultfilters import slugify

# Create your models here.

def upload_location(instance,filename):
	return "uploads/posts/%s/%s/%s" %(instance.category,instance.title_slug,filename)
class Category(models.Model):
	category = models.CharField(max_length=20,null=False,blank=False)

	class Meta:
		verbose_name_plural="Blog Category"

	def __str__(self):
		return self.category

class Post(models.Model):
	title  = models.CharField(max_length=100,blank=False,null=True)
	caption = models.CharField(max_length=300,blank=False,null=True)
	#category = models.CharField(max_length=20,null=True,blank=True,default='Others')
	category = models.OneToOneField(Category,related_name='cat')
	date = models.DateTimeField(auto_now_add=False,auto_now=True)
	content = RichTextUploadingField(config_name='default')
	preview_image = models.ImageField(upload_to=upload_location, blank=True,null=True)
	status = models.CharField(max_length=10,null=True,blank=True,default='Draft')
	featured = models.BooleanField(default=False)
	title_slug = models.SlugField(editable=False)
	blogauthor = models.CharField(max_length=20,blank=True,null=True,default="dopy")
	blogauthor_slug = models.SlugField(editable=False)
	link_to_post = models.URLField(null=True,blank=False,editable=False)

	def save(self, *args, **kwargs):
		self.title_slug = slugify(self.title)
		self.blogauthor_slug = slugify(self.blogauthor)
		self.link_to_post = 'http://'+Site.objects.get_current().domain+'/blogs/'+(self.blogauthor_slug).lower()+'/'+(self.category).category.lower()+'/'+(self.title_slug).lower()
		print(self.link_to_post)
		
		print(self.preview_image)
		print(self.blogauthor_slug)

		super(Post, self).save(*args, **kwargs)


def clean(sender,instance,**kwargs):
	try:
		remove_dir(os.path.join(settings.MEDIA_ROOT,"uploads","posts",str(instance.category).lower(),instance.title_slug))
	except Exception as e:
		print(e)
		pass
signals.post_delete.connect(clean,sender=Post)