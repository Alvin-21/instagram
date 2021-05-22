from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=150, null=True)
    image = CloudinaryField('image', null=True)

class Image(models.Model):
    image = CloudinaryField('image', null=True)
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=1500)
    posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class Likes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ForeignKey(Image, on_delete=models.CASCADE)


class Follow(models.Model):
	follower = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	following = models.ForeignKey(User,on_delete=models.CASCADE, null=True)