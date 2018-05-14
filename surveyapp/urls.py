from django.conf.urls import include, url
from django.contrib import admin
import survey.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(survey.urls)),
]
