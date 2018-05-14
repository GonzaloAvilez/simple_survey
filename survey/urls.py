from django.conf.urls import url
from django.contrib import admin
from . import views 


urlpatterns = [
	url(r'^$',views.SurveyPage.as_view(), name = 'questions'),
	url(r'^farewall/$',views.FarewallPage.as_view(), name = 'farewall'),
	
]