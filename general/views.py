# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from CodiPlatform.general.models import Album, Photo, Comment, Post
from CodiPlatform.registration.models import CustomUser
from CodiPlatform.codi.forms import WallCommentForm
def main(request):
    #if request.user.is_authenticated():
    #    return HttpResponseRedirect('/home/')
    #else:
    return render_to_response('main.html', context_instance = RequestContext(request))

def how_it_works(request):
    return render_to_response('how_it_works.html', context_instance = RequestContext(request))
    
@login_required
def home(request):#, user_id, garbage):
    print 'accessing home...'
    print request.user
    return render_to_response('home.html', context_instance = RequestContext(request))

@login_required
def album(request, id):
    try:
        requested = Album.objects.get(album_id = id)
    except Album.DoesNotExist:
        return render_to_response('http404.html', context_instance = RequestContext(request))
    photos = Photo.objects.filter(album=requested).order_by('position')
    requested.all_visit += 1
    requested.save()
    return render_to_response('album.html', {'photos' : photos, 'codi' : requested.owner, 'album' : requested}, context_instance = RequestContext(request))

@login_required
def post(request, id):
    try:
        requested = Post.objects.get(post_id = id)
    except Post.DoesNotExist:
        return render_to_response('http404.html', context_instance = RequestContext(request))
    
    if request.method == 'POST':
        print 'post?'
        form = WallCommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print 'valid?', cd['comment']

            custom_user = CustomUser.objects.get(user__username = request.user.username)
            Comment(message = cd['comment'], owner = custom_user, post = requested).save()

    comments = Comment.objects.filter(post=requested).order_by('-time_created')
    return render_to_response('post.html', {'form' : WallCommentForm(), 'post' : requested, 'comments' : comments,  'codi' : requested.owner}, context_instance = RequestContext(request))
