from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Profile, Image, Follow, Stream, Comment, Likes

# Create your views here.

def index(request):
    return render(request, 'index.html')