#!/usr/bin/env python
#-*- coding:utf-8 -*-


from musicplayer import helpers
from musicplayer.models import *

#import django.core.exceptions

def current_song(request):
	"""Give the currently played string from mpc back."""
	raw = helpers.getCurrentTitle()
	
	try:
		fine_title = Channel.objects.get(url = raw).name
	except Channel.DoesNotExist:
		try:
			fine_title = Title.objects.get(filepath = raw).name
		except Title.DoesNotExist:
			fine_title = raw
	
	return {
		'currently_playing' : fine_title
	}
