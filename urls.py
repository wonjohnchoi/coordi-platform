from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


import CodiPlatform.registration.views
import CodiPlatform.general.views
import CodiPlatform.codi.views
import CodiPlatform.setting.views
import CodiPlatform.message.views
import CodiPlatform.search.views

from CodiPlatform import settings

urlpatterns = patterns('',
                            
    # Examples:
    #url(r'^$', 'CodiPlatform.views.home', name='home'),
    # url(r'^CodiPlatform/', include('CodiPlatform.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^home/(\w+(.\w+)*)/$', CodiPlatform.home.views.home),
    url(r'^home/$', CodiPlatform.general.views.home),
    #url(r'^home/dashboard$', CodiPlatform.home.views.dashboard),
    #url(r'^home/inbox', CodiPlatform.home.views.inbox),
    #url(r'^home/profile', CodiPlatform.home.views.profile),

    url(r'^signup/$', CodiPlatform.registration.views.signup),
    url(r'^signup/thanks/$', CodiPlatform.registration.views.signup_thanks),
    url(r'^login/$', CodiPlatform.registration.views.custom_login),
    url(r'^logout/$', CodiPlatform.registration.views.custom_logout),
    url(r'^$', CodiPlatform.general.views.main),
    url(r'^info/how_it_works/$', CodiPlatform.general.views.how_it_works),
    url(r'^codi/([a-z0-9A-Z]+(\.[a-z0-9A-Z]+)*)/$', CodiPlatform.codi.views.codi),
    url(r'^codi/([a-z0-9A-Z]+(\.[a-z0-9A-Z]+)*)/gallery/(.*)$', CodiPlatform.codi.views.codi_gallery),
    url(r'^codi/([a-z0-9A-Z]+(\.[a-z0-9A-Z]+)*)/info/$', CodiPlatform.codi.views.codi_info),
    url(r'^codi/([a-z0-9A-Z]+(\.[a-z0-9A-Z]+)*)/wall/$', CodiPlatform.codi.views.codi_wall),
    url(r'^codi/([a-z0-9A-Z]+(\.[a-z0-9A-Z]+)*)/schedule/$', CodiPlatform.codi.views.codi_schedule),

    url(r'^codi/([a-z0-9A-Z]+(\.[a-z0-9A-Z]+)*)/consulting/$', CodiPlatform.codi.views.codi_consulting),
    url(r'^codi/([a-z0-9A-Z]+(\.[a-z0-9A-Z]+)*)/review/$', CodiPlatform.codi.views.codi_review),


    url(r'^codi/$', CodiPlatform.codi.views.my_codi),
    
    url(r'^showcase/$', CodiPlatform.codi.views.showcase),
    url(r'^showcase/([1-9]+)/([1-9]+)/$', CodiPlatform.codi.views.showcase_episode),
    url(r'^showcase/([1-9]+)/([1-9]+)/([1-9]+)/$', CodiPlatform.codi.views.showcase_part),

    
    
    url(r'^codiscoach/$', CodiPlatform.codi.views.codiscoach),
    url(r'^tryout/$', CodiPlatform.codi.views.tryout),
    url(r'^setting/account/$', CodiPlatform.setting.views.account_setting),
    url(r'^setting/codi/$', CodiPlatform.setting.views.codi_setting_push_album),
    url(r'^setting/codi/push_album/$', CodiPlatform.setting.views.codi_setting_push_album),
    url(r'^message/$', CodiPlatform.message.views.message),
    url(r'^search/$', CodiPlatform.search.views.codi_search),
    url(r'^album/(.+)/$', CodiPlatform.general.views.album),
    url(r'^post/(.+)/$', CodiPlatform.general.views.post),


    
    
    #redirect the result of 'login' view
    #url(r'^accounts/profile/$', CodiPlatform.home.views.home),
   # url(r'^accounts/login/$', login),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
