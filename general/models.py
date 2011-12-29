from django.db import models
import os, os.path
from binascii import hexlify
from CodiPlatform.registration.models import CustomUser
#from CodiPlatform.settings import basedir
import datetime
def _createId():
    return hexlify(os.urandom(16))

def _createPath(instance, filename):
    return os.path.join('photos', instance.photo_id)

'''
# Create your models here.
class User(models.Model):
    #user_id = models.CharField(max_length = 20, primary_key = True)
    first_name = models.CharField(max_length = 20, verbose_name = 'First Name:')#, min_length = 2)
    last_name = models.CharField(max_length = 20, verbose_name = 'Last Name:')#, min_length = 2)
    #profile_photo = models.ImageField(upload_to=os.path.join(os.path.dirname(__file__), 'photo/codi/%d'%codi_id))
    #email = models.CharField(verbose_name = 'Your Email:')
    
    def __unicode__(self):
        return '%s %s' %(self.first_name, self.last_name)
    '''
class TitlePhoto(models.Model):
    photo_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    #title = models.CharField(max_length=30)#, min_length = 4)
    image = models.ImageField(upload_to = _createPath)

class Theme(models.Model):
    season = models.PositiveIntegerField()
    episode = models.PositiveIntegerField()
    part = models.PositiveIntegerField()
    title = models.CharField(max_length = 50)

class Vote(models.Model):
    #season = models.PositiveIntegerField()
    #episode = models.PositiveIntegerField()
    #part = models.PositiveIntegerField()
    theme = models.ForeignKey(Theme)
    owner = models.ForeignKey(CustomUser)
    
#class ThemeBattle(models.Model):
#    album1 = models.m

class Album(models.Model):
    album_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    title = models.CharField(max_length=30)
    title_photo = models.OneToOneField(TitlePhoto)
    owner = models.ForeignKey(CustomUser)
    message = models.TextField(max_length=500)
    time_created = models.DateTimeField(auto_now_add = True, default=datetime.date.today())
    time_modified = models.DateTimeField(auto_now = True, default=datetime.date.today())
    category = models.CharField(max_length=40)
    unique_visit = models.PositiveIntegerField(default = 1)
    all_visit = models.PositiveIntegerField(default = 1)
    
    # if category is theme
    theme = models.ForeignKey(Theme, blank = True, null = True)
    time_voted = models.DateTimeField(default=datetime.date.today())
    elo = models.PositiveIntegerField(default = 1500)

    def __unicode__(self):
        return self.title

class Photo(models.Model):
    photo_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    #title = models.CharField(max_length=30)#, min_length = 4)
    image = models.ImageField(upload_to = _createPath)
    album = models.ForeignKey(Album)
    position = models.CharField(max_length=1)
    
    def __unicode__(self):
        return '%s #%s' %(self.album.title, self.position)

class Post(models.Model):
    post_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    owner = models.ForeignKey(CustomUser)
    message = models.TextField(max_length=500)
    time_created = models.DateTimeField(auto_now_add = True, default=datetime.date.today())
    time_modified = models.DateTimeField(auto_now = True, default=datetime.date.today())
    unique_visit = models.PositiveIntegerField(default = 1)
    all_visit = models.PositiveIntegerField(default = 1)

    def __unicode__(self):
        return self.owner.user.get_full_name()

class Comment(models.Model):
    comment_id = models.CharField(max_length=32, primary_key=True, default=_createId)
    #title = models.CharField(max_length=30)#, min_length = 4)
    owner = models.ForeignKey(CustomUser)

    message = models.TextField(max_length=100)
    time_created = models.DateTimeField(auto_now_add = True, default=datetime.date.today())
    time_modified = models.DateTimeField(auto_now = True, default=datetime.date.today())

    post = models.ForeignKey(Post)
    
    def __unicode__(self):
        return '%s' %(self.post.owner)

    