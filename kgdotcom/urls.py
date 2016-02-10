from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'home.views.index'),
    url(r'^admin/', include(admin.site.urls)),
]
