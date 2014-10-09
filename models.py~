#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.contrib import admin

from musicplayer import settings


# save every possible channel that could be available at this app
class Channel(models.Model):
	"""
	Specifies how webradio-channels are saved.
	From this Model is the playlist-file for mpc generated.

	related to :model:'auth.User'
	"""
	# title of the stream
	name 		= models.CharField(max_length = 60)

	# additional information you maybe want to store
	description = models.TextField(blank = True)

	# genre of the webstream
	genre		= models.CharField(max_length = 30, blank = True)

	#stream url
	url			= models.URLField()

	# how the titles are formatted in the stream information to get the
	# title informations in the status
	title_formatting = models.CharField(max_length = 255, blank = False)

	def __str__(self):
		return self.name

	"""def get_absolute_url(self):

		For automatic redirecting within the classbased views.
		You get redirected to the edit_channels overview.

		return reverse('edit_channels')"""


	class Meta:
		"""
		Additional informations to the Channel-Model.
		Permissions definied for the model.
		"""
		permissions = (
			('can_view', 'You can view this Model/App'),
			('can_control', 'You can control the Webradio'),
		)



"""
def mpc_update(modeladmin, request, queryset):

	Adminaction for updating the MPC if you changed things within the Admininterface.
	This does the same thing as saving/creating Channels in the UI.

	#manageMPC()
mpc_update.short_description = "Updates the MPC on your PI" """



class ChannelAdmin(admin.ModelAdmin):
	"""
	Pretties the Admininterface of the Channels up.
	Some Ordering stuff and so on.
	"""
	# how the fields are ordered in the edit view of the admininterface
	fields = (('name', 'genre'), 'url', 'description')

	# how things are displayed in the listview for all objects
	list_display = ('name', 'url', 'genre')


class ChannelForm(ModelForm):
	"""
	Generic ModelForm for the Channel.
	"""
	class Meta:
		model = Channel
		#fields = '__all__'





################################################################################
class Band(models.Model):
	"""Model for saving bands. They have relations to titles and to Albums."""
	# bandname
	name		= models.CharField(max_length = 100)

	# more not needed at the moment

	def __unicode__(self):
		return self.name




class Album(models.Model):
	"""Model for saving published albums by bands. A Album has relations to
	titles, which are in the album."""
	# album name
	name		= models.CharField(max_length = 100)

	# artists who published it
	interprets 	= models.ManyToManyField(Band, null = True, blank = True)

	def __unicode__(self):
		return self.name



class Title(models.Model):
	"""Model for saving the music titles. They are related to Artists/Bands
	and albums. The database save the filepath relative to the mpd-music-dir,
	which is usually /var/lib/mpd/music."""
	# title name
	name		= models.CharField(max_length = 100)

	# filepath for playing in mpd
	filepath	= models.CharField(max_length = 100, blank = True)

	# on which album published
	album		= models.ManyToManyField(Album, blank = True, null = True)

	# which artists wrote the title
	interprets	= models.ManyToManyField(Band, blank = True, null = True)

	# which genre it is, for sorting and searching purposes
	genre		= models.CharField(max_length = 30, blank = True)

	def __unicode__(self):
		return self.name


class Playlist(models.Model):
	"""Model to save userdefined playlists for mpc."""
	# playlistname
	name 		= models.CharField(max_length = 100)

	titles		= models.ManyToManyField(Title, blank = True, null = True)
	
	def __unicode__(self):
		return self.name
