# Create your views here.

from django.contrib.auth.decorators import login_required
from CodiPlatform.general.models import Album, Post, Theme, Vote, Photo

from CodiPlatform.registration.models import CustomUser
from CodiPlatform.registration.views import find_customuser
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from CodiPlatform.codi.forms import WallPostForm
from CodiPlatform.settings import SHOWCASE_VOTES
from django.db.models import Q

@login_required
def codi(request, codi_id, garbage):
    print 'accessing codi/codi'
    print 'codi_id:', codi_id
    return HttpResponseRedirect('/codi/%s/wall/' % codi_id)

def get_customuser(request, codi_username):
    try:
        codi = CustomUser.objects.exclude(codi=None).get(user__username = codi_username)
        print 'Codi name:', codi.user.get_full_name()
        return codi
    except CustomUser.DoesNotExist:
        print 'no such codi'
        return render_to_response('http404.html', context_instance = RequestContext(request))
@login_required
def codi_gallery(request, codi_id, garbage, category):
    if request.user.username == codi_id:
        print 'hey owner!'

    codi = get_customuser(request, codi_id)
    albums = Album.objects.filter(owner = codi)
    sections = []
    if category == '' or category.startswith('sample'):
        sections.append(('Sample', albums.filter(category = 'sample').order_by('-time_created')))
    if category == '' or category.startswith('review'):
        sections.append(('Review', albums.filter(category = 'review').order_by('-time_created')))
    if category == '' or category.startswith('theme'):
        sections.append(('Previous Themes', albums.filter(category = 'theme').order_by('-time_created')))
    if category == '' or category.startswith('episode'):
        sections.append(('Previous Episodes', albums.filter(category = 'episode').order_by('-time_created')))
    return render_to_response('codi_gallery.html', {'codi' : codi, 'sections' : sections}, context_instance = RequestContext(request))


@login_required
def codi_info(request, codi_id, garbage):
    codi = get_customuser(request, codi_id)
    return render_to_response('codi_info.html', {'codi' : codi}, context_instance = RequestContext(request))
@login_required
def codi_wall(request, codi_id, garbage):
    codi = get_customuser(request, codi_id)
    form = None
    is_page_owner = False
    
    if request.user.username == codi_id:
        is_page_owner = True
        if request.method == 'POST':
        
            form = WallPostForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                Post(message = cd['post'], owner = codi).save()
                
    posts = Post.objects.filter(owner = codi).order_by('-time_modified')
    print is_page_owner
    print WallPostForm().as_ul()
    return render_to_response('codi_wall.html', {'codi' : codi, 'form' : WallPostForm(), 'is_page_owner' : is_page_owner, 'posts' : posts}, context_instance = RequestContext(request))
@login_required
def codi_schedule(request, codi_id, garbage):
    codi = get_customuser(request, codi_id)
    return render_to_response('codi_schedule.html', {'codi' : codi}, context_instance = RequestContext(request))
@login_required
def codi_consulting(request, codi_id, garbage):
    codi = get_customuser(request, codi_id)
    return render_to_response('codi_consulting.html', {'codi' : codi}, context_instance = RequestContext(request))
@login_required
def codi_review(request, codi_id, garbage):
    codi = get_customuser(request, codi_id)
    return render_to_response('codi_review.html', {'codi' : codi}, context_instance = RequestContext(request))


def trash(request, codi_id):
    page_to_render = 'codi_gallery.html'
    if request.method == 'GET':
        if 'sm' in request.GET:
            if request.GET['sm'] == 'info':
                page_to_render = 'codi_info.html'
            elif request.GET['sm'] == 'schedule':
                page_to_render = 'codi_schedule.html'
            elif request.GET['sm'] == 'consulting':
                page_to_render = 'codi_consulting.html'
            elif request.GET['sm'] == 'review':
                page_to_render = 'codi_review.html'
            elif request.GET['sm'] == 'wall':
                page_to_render = 'codi_wall.html'
    if page_to_render == 'codi_gallery.html':
        print 'visiting gallery!'
        print 'codi:', codi
    else:
        albums = None

@login_required
def my_codi(request):
    return HttpResponseRedirect('/codi/%s/'%request.user.username)

from CodiPlatform.settings import SEASON, EPISODE

@login_required
def showcase(request):
    return HttpResponseRedirect('/showcase/%d/%d/' % (SEASON, EPISODE))

@login_required
def showcase_episode(request, requested_season, requested_episode):
    themes = Theme.objects.filter(season = requested_season, episode = requested_episode).order_by('part')
    return render_to_response('showcase_episode_menu.html', {'themes' : themes, 'season' : requested_season, 'episode' : requested_episode}, context_instance = RequestContext(request))
@login_required
def showcase_part(request, requested_season, requested_episode, requested_part):
    try:
        requested_theme = Theme.objects.get(season = requested_season, episode = requested_episode, part = requested_part)
    except Theme.DoesNotExist:
        return render_to_response('http404.html', context_instance = RequestContext(request))
    
    
        
    if requested_season == str(SEASON) and requested_episode == str(EPISODE):
        if request.method == 'POST':
            print('post request')
            pass
        
        votes = Vote.objects.filter(theme = requested_theme, owner__user = request.user)
        print('getting all votes by this user for this theme')
        if votes.count() < SHOWCASE_VOTES:
            print ('# votes = %d' % (votes.count()))
            albums = Album.objects.filter(theme = requested_theme).order_by('time_voted')
            print ('# albums = %d' % (albums.count()))

            if albums.count() < 2:
                return render_to_response('http404.html', context_instance = RequestContext(request))
            album1 = albums[0]
            albums = albums.exclude(owner = album1.owner)
            
            #albums = albums.exclude([1:]
            album2 = None
            
            elo1 = album1.elo
            for gap in range(100, 301, 100):
                min = elo1 - gap
                max = elo1 + gap
                tmp = albums.filter(Q(elo__lt = max) & Q(elo__gt = min))
                if tmp.count() > 0:
                    album2 = tmp[0]
                    break
            if album2 is None:
                album2 = albums[1]
            photos1 = Photo.objects.filter(album=album1).order_by('position')
            photos2 = Photo.objects.filter(album=album2).order_by('position')

            print('album1', album1.title)
            print('album2', album2.title)
            #for album in albums:
            #    print(album.title, album.time_modified)
            return render_to_response('showcase_vote.html', {'theme' : requested_theme, 'album1' : album1, 'album2' : album2, 'photos1' : photos1, 'photos2' : photos2}, context_instance = RequestContext(request))
    print('showing rank')
    return render_to_response('showcase_rank.html', {'theme' : requested_theme}, context_instance = RequestContext(request))


@login_required
def codiscoach(request):
    return render_to_response('codiscoach.html', context_instance = RequestContext(request))

@login_required
def tryout(request):
    return render_to_response('tryout.html', context_instance = RequestContext(request))
