from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Profile, Image, Follow, Stream, Comment, Likes
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    images = Stream.objects.filter(user=user)

    group_ids = []

    for image in images:
        group_ids.append(image.image_id)
        
    image_items = Image.objects.filter(id__in=group_ids).all().order_by('-posted')

    return render(request, 'index.html', {"image_items": image_items})


@login_required(login_url='/accounts/login/')
def new_image(request):
    user = request.user.id

    if request.method == "POST":
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')
        
        i, created = Image.objects.get_or_create(image=image, caption= caption, user_id=user)
        i.save()
        return redirect('index')

    else:
        form = NewImageForm()

    return render(request, 'new_image.html', {"form": form})