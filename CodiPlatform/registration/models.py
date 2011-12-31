from django.db import models
from django.contrib.auth.models import User
#from CodiPlatform.general.models import Photo
# Create your models here.
# Create your models here.

class Codi(models.Model):
    birthday = models.DateField(blank = True)
    info = models.TextField()
    website = models.URLField(blank = True)
    #profile_photo = models.OneToOneField(Photo)


from CodiPlatform.settings import SHOWCASE_VOTES
class CustomUser(models.Model):
    #user_id = models.CharField(max_length = 20, primary_key = True)
    #profile_photo = models.ImageField(upload_to=os.path.join(os.path.dirname(__file__), 'photo/codi/%d'%codi_id))
    user = models.OneToOneField(User)
    codi = models.OneToOneField(Codi, null = True, blank = True)
    accum_point = models.IntegerField(default = 0)
    accum_cach = models.IntegerField(default = 0)
    point = models.IntegerField(default = 0)
    cash = models.IntegerField(default = 0)
    #accum_votes = models.PositiveIntegerField(default = 0)
    #required_votes = models.PositiveIntegerField(default = SHOWCASE_VOTES)
    #other = models.ManyToManyField('self', through = 'Message')
    
    #profile_photo = models.OneToOneField(Photo, unique = True)
    #messages = models
    #def vote(self):
    #    self.accum_votes += 1
    #    self.required_votes -= 1

    def __unicode__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)



class Message(models.Model):
    content = models.TextField(max_length = 500)
    time = models.DateTimeField(auto_now_add = True)
    sender_id = models.CharField(max_length = 30)
    recipient_id = models.CharField(max_length = 30)
