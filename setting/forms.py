from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import Select, CheckboxSelectMultiple
from CodiPlatform.general.models import Theme, Album

'''
Created on Dec 24, 2011

@author: wonjohnchoi
'''
from CodiPlatform.settings import SEASON, EPISODE
from django import forms

class AlbumForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AlbumForm, self).__init__(*args, **kwargs)

    title = forms.CharField(max_length = 50)
    title_photo = forms.ImageField(max_length = 500)
    photo1  = forms.ImageField(max_length = 500, required=False)
    photo2  = forms.ImageField(max_length = 500, required=False)
    photo3  = forms.ImageField(max_length = 500, required=False)
    photo4  = forms.ImageField(max_length = 500, required=False)
    photo5  = forms.ImageField(max_length = 500, required=False)
    photo6  = forms.ImageField(max_length = 500, required=False)
    message = forms.CharField(widget=forms.Textarea)
    category = ChoiceField(widget=Select,
        choices=(('sample', 'Sample'), ('review', 'Review'),
        ('market', 'Make a coordi for clients')) +
        tuple(('theme|%d|%d|%d' % (SEASON, EPISODE, theme.part), 'Theme Battle - %s' %theme.title) for theme in Theme.objects.filter(season=SEASON, episode=EPISODE)))
    
    #def __init__(self, user, *args, **kwargs):
    #    super(AlbumForm, self).__init__(*args, **kwargs)
        
    #    if not user.is_authenticated():
    #        self.fields['captcha'] = AlbumForm()

    
    def clean_category(self):
        category =  self.data['category']
        if category.startswith('theme'):
            data = category.split('|')
            print data
            if data[1] != unicode(SEASON) or data[2] != unicode(EPISODE) or len(data) != 4:
                raise forms.ValidationError('SEASON or EPISODE do not match.')
            
            try:
                Theme.objects.get(season = data[1], episode = data[2], part = data[3])
            except Theme.DoesNotExist:
                raise forms.ValidationError('PART do not match.')
            try:
                Album.objects.get(owner__user = self.request.user, theme__season = data[1], theme__episode = data[2])
                raise forms.ValidationError('You already submitted an album for season %s - episode %s.' %(data[1], data[2]))
            except Album.DoesNotExist:
                pass
            return data
        return category
    def clean(self,*args, **kwargs):
        self.clean_category()
        #self.clean_title()
        return super(AlbumForm, self).clean(*args, **kwargs)
    