from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^sandeshahm', hello.views.sandeshahm, name='sandeshahm'),
    url(r'^sandeshraj', hello.views.sandeshraj, name='sandeshraj'),
    url(r'^sandeshbar', hello.views.sandeshbar, name='sandeshbar'),
    url(r'^sandeshsur', hello.views.sandeshsur, name='sandeshsur'),
    url(r'^sendnewssandesh', hello.views.sendnewssandesh, name='sendnewssandesh'),
    url(r'^othertie', hello.views.othertie, name='othertie'),
    url(r'^otherfe', hello.views.otherfe, name='otherfe'),
    url(r'^othertt', hello.views.othertt, name='othertt'),
    url(r'^othertoi', hello.views.othertoi, name='othertoi'),
    url(r'^sendnewsother', hello.views.sendnewsother, name='sendnewsother'),
    url(r'^dbahm', hello.views.dbahm, name='dbahm'),
    url(r'^dbraj', hello.views.dbraj, name='dbraj'),
    url(r'^dbbar', hello.views.dbbar, name='dbbar'),
    url(r'^dbsur', hello.views.dbsur, name='dbsur'),
    url(r'^gsahm', hello.views.gsahm, name='gsahm'),
    url(r'^gsraj', hello.views.gsraj, name='gsraj'),
    url(r'^gsbar', hello.views.gsbar, name='gsbar'),
    url(r'^gssur', hello.views.gssur, name='gssur'),
    url(r'^dabsur', hello.views.dabsur, name='dabsur'),
    url(r'^dabdel', hello.views.dabdel, name='dabdel'),
    url(r'^sendnewsdb', hello.views.sendnewsdb, name='sendnewsdb'),
    url(r'^sendnewsgs', hello.views.sendnewsgs, name='sendnewsgs'),
    url(r'^sendnewsdab', hello.views.sendnewsdab, name='sendnewsdab'),
    path('admin/', admin.site.urls),

]
