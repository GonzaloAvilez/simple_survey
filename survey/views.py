from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic 
from .forms import RequestSurveyForm
from django.contrib import messages



class SurveyPage(generic.edit.FormView):
	template_name = "survey/survey.html"
	form_class = RequestSurveyForm
	success_url = '/farewall/'
	
	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			form.save()
			return self.form_valid(form, **kwargs)
		else:
			return self.form_invalid(form, **kwargs)


class FarewallPage(generic.TemplateView):
	template_name = "survey/farewall.html"

