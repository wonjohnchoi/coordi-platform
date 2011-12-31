'''
Created on Dec 18, 2011

@author: wonjohnchoi
'''

from django.contrib import admin
from CodiPlatform.registration import models
admin.site.register(models.CustomUser)
admin.site.register(models.Codi)
admin.site.register(models.Message)
