# Create your views here.

from django.contrib.auth.decorators import login_required
from CodiPlatform.registration.models import CustomUser
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from CodiPlatform.setting.forms import AlbumForm
from CodiPlatform.registration.views import find_codi, find_customuser
from CodiPlatform.general.models import Album, Photo, TitlePhoto, Theme
from CodiPlatform.general.models import _createId;

@login_required
def account_setting(request):
    return render_to_response('setting_account.html', context_instance = RequestContext(request))

@login_required
def codi_setting(request):
    if not find_codi(request.user.username):
        return HttpResponseRedirect('/home/')
    

    if find_codi(request.user.username):
        return render_to_response('setting_codi_sidebar.html', context_instance = RequestContext(request))
    else:
        pass
    
def handle_uploaded_file(f):
    destination = open('some/file/name.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

from CodiPlatform.settings import STATIC_ROOT
import os.path
import Image
@login_required
def codi_setting_push_album(request):
    if not find_codi(request.user.username):
        return HttpResponseRedirect('/home/')
    
    album = None
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, request=request)
        print 'post!'
        if form.is_valid():
            print('form valid!')
            cd = form.cleaned_data
            new_title = cd['title']
            new_message = cd['message']
            new_category = cd['category']
            new_theme = None
            if new_category[0] == 'theme':
                new_theme = Theme.objects.get(season = new_category[1], episode = new_category[2], part = new_category[3])
                new_category = 'theme'
            print 'category', new_category
            print 'cd', cd
            images = [cd['photo1'], cd['photo2'], cd['photo3'], cd['photo4'], cd['photo5'], cd['photo6']]

            new_title_photo = TitlePhoto(image = cd['title_photo'])
            new_title_photo.save()
            new_album = Album(title = new_title, title_photo = new_title_photo, owner = find_customuser(request.user), message = new_message, category = new_category, theme = new_theme)
            new_album.save()

            print('nice form!')
            pos = 1
            for new_image in images:
                
                print 'looing image #', pos
                print new_image
                '''
                if new_image == None:
                    #Photo(album = new_album, position = str(pos)).save()
                    print 'image', UploadedFile(os.path.join(STATIC_ROOT, 'default_image'))
                    #new_image = Image.open(os.path.join(STATIC_ROOT, 'default_image')).read()
                new_photo = Photo(image = new_image, album = new_album, position = str(pos))
                print 'new_photo_image',new_photo.image
                if not new_photo.image:
                    print 'NONE!'
                    new_photo.image.save(os.path.join('photos', new_photo.photo_id), File(open(os.path.join(STATIC_ROOT, 'default_image'))))
                new_photo.save()
                '''
                print type(new_image)
                if new_image is not None:
                    new_photo = Photo(image = new_image, album = new_album, position = str(pos))
                    new_photo.save()
                    
                pos += 1
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/setting/codi/push_album/?uploaded=%s'%new_album.album_id)
    else:
        form = AlbumForm(request = request)
        if request.method == 'GET':
            if 'uploaded' in request.GET:
                id = request.GET['uploaded']
                try:
                    album = Album.objects.get(album_id = id)
                except Album.DoesNotExist:
                    album = None
    return render_to_response('setting_codi_push_album.html', {'form': form, 'uploaded': album}, context_instance = RequestContext(request))

    
        