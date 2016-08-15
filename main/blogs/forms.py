from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

class PostForm(forms.ModelForm):

	CHOICES_STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    )

	title = forms.CharField(required=True)
	content = forms.CharField(widget=CKEditorUploadingWidget())
	status = forms.ChoiceField(choices=CHOICES_STATUS)