from django.contrib import admin
from .models import Image, Follow, Stream

# Register your models here.

admin.site.register(Image)
admin.site.register(Follow)
admin.site.register(Stream)