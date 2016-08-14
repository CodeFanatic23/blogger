from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

class PostForm(forms.ModelForm):
	# CHOICES = (
 #        ('news', 'News'),
 #        ('red-cross-stories', 'Red Cross Stories'),
 #        ('disaster', 'Disaster'),
 #        ('courses', 'Academic Courses'),
 #        ('community', 'Community'),
 #        ('alerts', 'Alerts'),
 #        ('other','Other'),
 #    )
	CHOICES_STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    )

	title = forms.CharField(required=True)
	content = forms.CharField(widget=CKEditorUploadingWidget())
	# category = forms.ChoiceField(choices=CHOICES)
	status = forms.ChoiceField(choices=CHOICES_STATUS)