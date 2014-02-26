from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
	'web.views',
	url(r'^$', 'events.index', name='web.index'),
	url(r'^add/$', 'events.add_event', name='web.add_event'),
	url(r'^view/(?P<event_id>\d+)/(?P<slug>[-\w]+)/$', 'events.view_event', name='web.view_event'),
	url(r'^thankyou/$', 'events.thankyou', name='web.thankyou'),
	url(r'^guide/$', 'events.guide', name='web.guide'),
	url(r'^login/$', 'users.login', name='web.login'),
	url(r'^approved/(?P<country_code>\w{2,3})/$',"events.list_approved_events",name="web.list_events"),
	url(r'^pending/(?P<country_code>\w{2,3})/$', "events.list_pending_events",name="web.pending_events"),
	)
