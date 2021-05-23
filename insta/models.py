from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=150, null=True)
    image = CloudinaryField('image', null=True)

    def __str__(self):
        return self.first_name

    def save_profifle(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_bio(cls, id, text):
        cls.objects.filter(id=id).update(bio=text)

class Image(models.Model):
    image = CloudinaryField('image', null=True)
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=1500)
    posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls, id, text):
         cls.objects.filter(id=id).update(caption=text)

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class Likes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='post_like')


class Follow(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='follower')
    following = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='following')


class Stream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='stream_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()

    def add_image(sender, instance, *args, **kwargs):
    	image = instance
    	user = image.profile
    	followers = Follow.objects.all().filter(following=user)
    	for follower in followers:
    		stream = Stream(image=image, user=follower.follower, date=image.posted, following=user)
    		stream.save()

post_save.connect(Stream.add_image, sender=Image)