from django.conf.urls.defaults import patterns, include, url
import councilmatic_customizations as custom

urlpatterns = patterns('',
    # url('^...$', custom.views....),
    
    (r'^', include('councilmatic.urls')),
)
