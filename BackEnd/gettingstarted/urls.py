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
    path('admin/', admin.site.urls),

]
