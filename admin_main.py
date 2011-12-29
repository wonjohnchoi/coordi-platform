'''
Created on Dec 23, 2011

@author: wonjohnchoi
'''
from django.contrib.auth.models import User
from CodiPlatform.registration.models import Message
for user in User.objects.all():
    msg = Message(content = 'Hey! Welcome to Coordi&Coach', recipient_id = "admin", sender_id = user.username)
    msg.save()