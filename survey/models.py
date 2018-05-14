# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.auth.models import User
from .choices import * 
 


class Question(models.Model):
	""" Simple way to make anonymous users(UUID) for each  survey session"""
	questionnaire_id = models.AutoField(primary_key=True) 
	user = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
	service_query = models.IntegerField(choices=SURVEY_CHOICES, default=None)
	fastfood_query = models.IntegerField(choices=SURVEY_CHOICES, default=None)

	def __str__(self):
		return '{}'.format(self.questionnaire_id)