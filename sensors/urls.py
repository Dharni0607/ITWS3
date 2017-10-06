from django.conf.urls import url
from . import views

app_name='sensors'

urlpatterns = [
    # /sensors/
    url(r'^$', views.aaa , name='index'),
    url(r'^display/$', views.new_disp, name="new_disp"),url(r'^display/(?P<temperature>[0-9]+.[0-9]+)/(?P<humidity>[0-9]+.[0-9]+)/(?P<ps1>[0-9]+.[0-9]+)/(?P<as1>[\w\-]+)/(?P<ps2>[0-9]+.[0-9]+)/(?P<as2>[\w\-]+)/(?P<wl>[0-9]+.?[0-9]*)/',views.Display,name="Display"),
]
