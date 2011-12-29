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

@login_required
def message(request):
    #custom_user = CustomUser.objects.get(user = request.user)
    user = request.user
    
    other_ids = set()
    for msg in Message.objects.filter(sender_id = user.username):
        other_ids.add(msg.recipient_id)
    for msg in Message.objects.filter(recipient_id = user.username):
        other_ids.add(msg.sender_id)
    print other_ids
    
    other_users = []
    for user_id in other_ids:
        print 'other_user:', user_id
        if user_id != 'admin':
            other_users.append(User.objects.get(username = user_id))
    other_users.sort(key = lambda other: other.first_name)
    print other_users
    # others = CustomUser.objects.filter(other = request.user).order_by('first_name', 'last_name')
    context = {'others' : other_users, 'messages' : None}
    
    if request.method != 'GET' or 'sm' not in request.GET or request.GET['sm'] == '__all':
        target = None
    else:
        try:
            target = CustomUser.objects.get(user__username = request.GET['sm']).user
            target_name = target.username
            print 'target:', target_name
            context['messages'] = Message.objects.all().filter((Q(sender_id = user.username) & Q(recipient_id = target_name))
                                                         | (Q(recipient_id = user.username) & Q(sender_id = target_name))).order_by('-time')
        except CustomUser.DoesNotExist:
            target = None
            print 'no such target!'
    #print custom_user.user.username
    #print Message.objects.filter(sender = custom_user)
    #select all
    if target is None:
        context['messages'] = Message.objects.all().filter(Q(sender_id = user.username) | Q(recipient_id = user.username)).order_by('-time')
            
    return render_to_response('message.html', context, context_instance = RequestContext(request))
