from django.contrib import admin
from .models import *


class QuestionAdmin(admin.ModelAdmin):
	list_display = ['questionnaire_id','user','service_query','fastfood_query']

admin.site.register(Question,QuestionAdmin)	

