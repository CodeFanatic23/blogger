# blogger
A blogging application built in django using ckeditor and comments using disqus.

#Installation

Download or Clone the repository

Install dependencies using:

``pip install -r requirements.txt``

Add the following to your settings.py:
  
``CKEDITOR_UPLOAD_PATH = "ckeditor/"``

``CKEDITOR_IMAGE_BACKEND = 'pillow'``

``CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'``

``CKEDITOR_CONFIGS = {'default': {``

       'toolbar': 'full',
       
       'height': 300,
       
       'width': 800,
       
       'skins':'icyorange',
       
    },
    
``}``

``CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True``

``CKEDITOR_BROWSE_SHOW_DIRS = True``

``CKEDITOR_CONFIGS = {``

    'default': {
        'toolbar': (
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
            
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
            
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            
            ['Link', 'Unlink', 'Anchor'],
            
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            
            ['Styles', 'Format', 'Font', 'FontSize'],
            
            ['TextColor', 'BGColor'],
            
            ['Maximize', 'ShowBlocks', '-', 'About', 'pbckcode'],
            
        ),
  `` }``
   
``}``

``SITE_ID = 1``

``SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')``

``DISQUS_API_KEY = 'your_disqus_key'``

``DISQUS_WEBSITE_SHORTNAME = 'your_disqus_shortname'``

Add the following to ``INSTALLED APPS``:

    'disqus',
    
    'ckeditor',
    
    'ckeditor_uploader',
    
    'crispy_forms',
    
    'blogs',
    
    
You Will Also need to set up your media and static properly

Copy All the templates from templates folder to your templates. Alternatively you can also add it to ``TEMPLATES:{'DIRS:[],}'``

Copy the blogs folder to your project.

Add following urls to urls.py:

    from django.conf.urls.static import static
    from blogs.views import *
    from django.conf import settings
    from django.conf.urls import include
    
    url(r'^blogs/$', blogHome,name='blogHome'),
    url(r'^blogs/(?P<blogauthor>[0-9A-Za-z_\-]+)/$', authorHome,name='authorHome'),
    url(r'^blogs/(?P<blogauthor>[0-9A-Za-z_\-]+)/(?P<category>[0-9A-Za-z_\-]+)/$', category,name='category'),
    url(r'^blogs/(?P<blogauthor>[0-9A-Za-z_\-]+)/(?P<category>[0-9A-Za-z_\-]+)/(?P<blogname>[0-9A-Za-z_\-]+)/$', blogView,name='blogview'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

Run:

``python manage.py makemigrations``

``python manage.py migrate``
