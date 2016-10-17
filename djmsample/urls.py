from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

admin.site.site_header = 'Djmongo Administration'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.djmongo.console.urls')),
    url(r'^console/', include('apps.djmongo.console.urls')),
    url(r'^search/', include('apps.djmongo.search.urls')),
    url(r'^import/', include('apps.djmongo.dataimport.urls')),
    url(r'^accounts/', include('apps.djmongo.accounts.urls')),
    url(r'^write/', include('apps.djmongo.write.urls')),
    url(r'^aggregations/', include('apps.djmongo.aggregations.urls')),

]
