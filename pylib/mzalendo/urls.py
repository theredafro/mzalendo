from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('core.views',
    # Homepage
    url(r'^$', 'home', name='home'),

    # Lists
    url(r'^person/all/',       'person_list',       name='person_list'),
    url(r'^place/all/',        'place_list',        name='place_list'),
    url(r'^organisation/all/', 'organisation_list', name='organisation_list'),
    
    # Objects
    url(r'^person/(?P<slug>[-\w]+)/',       'person',       name='person'),
    url(r'^position/(?P<slug>[-\w]+)/',     'position',     name='position'),

    url(r'^place/is/(?P<slug>[-\w]+)/', 'place_kind', name='place_kind'),
    url(r'^place/(?P<slug>[-\w]+)/',    'place',      name='place'),

    url(r'^organisation/is/(?P<slug>[-\w]+)/', 'organisation_kind', name='organisation_kind'),
    url(r'^organisation/(?P<slug>[-\w]+)/', 'organisation', name='organisation'),

    # specials
    url(r'^parties', 'parties', name='parties'),


    # Haystack
    url(r'^search/', include('haystack.urls') ),

    # Ajax select
    url(r'^ajax_select/', include('ajax_select.urls')),
)

# Accounts
urlpatterns += patterns('',
    (r'^accounts/', include('registration.backends.default.urls')),
)

# Comments
urlpatterns += patterns('',    
    (r'^comments/', include('mz_comments.urls')),
)

# Info pages
urlpatterns += patterns('',
    (r'^info/', include('info.urls')),
)

# Hansard pages
urlpatterns += patterns('',
    (r'^hansard/', include('hansard.urls')),
)

# Admin
urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# serve some pages directly from templates
urlpatterns += patterns('',
    url(r'^privacy/$', direct_to_template, {'template': 'privacy.html'}, name='privacy'),
)

# serve media_root files if needed (/static served in dev by runserver)
if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        (   r'^media_root/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT }
        ),
    )


