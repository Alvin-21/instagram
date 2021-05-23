from django.test import TestCase
from .models import Profile, Image
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTest(TestCase):
    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()
    
    def setUp(self):
        self.john = Profile(first_name='John', last_name='Doe', bio='This is my profile page')

    def test_instance(self):
        self.assertTrue(isinstance(self.john, Profile))
    
    def test_save_method(self):
        self.john.save_profifle()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_method(self):
        self.john.save_profifle()
        self.john.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

    def test_update_bio(self):
        self.john.save_profifle()
        self.john.update_bio(self.john.id, 'This is my new bio')
        profile = Profile.objects.filter(bio='This is my new bio')
        self.assertTrue(len(profile) == 1)


class ImageTest(TestCase):
    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()

    def setUp(self):
        self.user = User.objects.create_user('john', email=None, password='secretpassword')
        self.pic = Image(name='mustang', caption='cool car', profile=self.user, likes=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.pic, Image))

    def test_save_method(self):
        self.pic.save_image()
        pic = Image.objects.all()
        self.assertTrue(len(pic) > 0)