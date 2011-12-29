# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from CodiPlatform.registration.models import CustomUser
from CodiPlatform.registration.models import Message
from django.db.models import Q

def codi_search(request):
    if request.method == 'GET' and 'arg' in request.GET:
        arg = request.GET['arg']
        results = CustomUser.objects.exclude(codi = None).filter(Q(user__first_name__istartswith = arg) | Q(user__last_name__istartswith = arg) | Q(user__username__istartswith = arg))
        return render_to_response('search.html', {'results' : results}, context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('/home/')