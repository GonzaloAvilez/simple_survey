# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import *
from .choices import *


class RequestSurveyForm(forms.ModelForm):

	def __init__(self,*args, **kwargs):
		super(RequestSurveyForm,self).__init__(*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_action = '#'
		self.helper.layout = Layout(
			Field('service_query'),
			Field('fastfood_query'),

            Submit('update', 'Aceptar', css_class="btn-success"),

			)

	class Meta:
		model = Question
		fields = ['service_query','fastfood_query',]
		labels = {
            'service_query': '¿Cómo calificaría el servicio de la plaza?',
            'fastfood_query' : '¿Cómo calificaría el servicio del fastfood?',
        }



