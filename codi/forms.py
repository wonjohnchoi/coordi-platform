'''
Created on Dec 22, 2011

@author: wonjohnchoi
'''

from django.forms import ModelForm
from django import forms
from CodiPlatform.registration.models import CustomUser
class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        exclude = ('user')

class WallPostForm(forms.Form):
    post = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows':'5','cols':'70'}), min_length=1)
    

    def clean_post(self):
        if not (1 <= len(self.data['post']) <= 500):
            raise forms.ValidationError('Must be less or equal to 500 characters')
        return self.data['post']
    
    def clean(self,*args, **kwargs):
        self.clean_post()
        return super(WallPostForm, self).clean(*args, **kwargs)

class WallCommentForm(forms.Form):
    comment = forms.CharField(max_length=100, widget=forms.Textarea, min_length=1)
    

    def clean_comment(self):
        if not (1 <= len(self.data['comment']) <= 100):
            raise forms.ValidationError('Must be less or equal to 500 characters')
        return self.data['comment']
    
    def clean(self,*args, **kwargs):
        self.clean_comment()
        return super(WallCommentForm, self).clean(*args, **kwargs)

    