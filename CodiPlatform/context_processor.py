'''
Created on Dec 22, 2011

@author: wonjohnchoi
'''
from CodiPlatform.registration.models import CustomUser
def custom_user(request):
    if request.user.is_authenticated():
        try:
            return {'custom_user' : CustomUser.objects.get(user = request.user)}
        except CustomUser.DoesNotExist:
            return {'custom_user' : None}
    else:
        return {'custom_user': None}
