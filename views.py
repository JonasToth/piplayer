#!/usr/bin/env python
#-*- coding:utf-8 -*-


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseForbidden
from django.core.urlresolvers import reverse, reverse_lazy

from django.contrib.auth.models import User
from musicplayer.models import *

from django.views.generic.edit import UpdateView, CreateView, DeleteView, ModelFormMixin
from django.views.generic.list import ListView

from musicplayer import helpers
from musicplayer import filemanagement
from musicplayer.settings import WEBRADIO_PLAYLIST_NAME




# index of the musicplayerapp
def playerIndex(request):
	"""
	View for all my channels. You can control your musicplayer from this view.
	"""
	template_name = 'musicplayer/index.html'

	radioChannels 	= Channel.objects.all()
	albumList		= Album.objects.all()
	playlist		= Playlist.objects.all()

	return render(request, template_name,
		{
			"channels" 	: radioChannels,
			"albums" 	: albumList,
			"pls_test"  : playlist,
		})




# updating a channel
class ChannelUpdate(UpdateView):
	"""
	Creates the View for Updating a channel.
	It updates the MPC playlist aswell after saving the channel to the database.
	"""
	model = Channel
	fields = ['name', 'url', 'description', 'genre',]
	#template_name = 'musicplayer/channel_update.html'
	success_url = reverse_lazy('player_index')
	url = reverse_lazy('player_edit_radio')

	def form_valid(self, form):
		"""
		Overrides the saving-procedure of the Generic Views for own purposes.
		Updates the MPC.
		"""
		helpers.createWebradioPlaylist()
		return super(ChannelUpdate, self).form_valid(form)


# create channels
class ChannelCreate(CreateView):
	"""
	Creates a new Channel. You are subscribed to it automatically.
	It updates the MPC playlist aswell after saving the channel to the database.
	"""
	model = Channel
	fields = ['name', 'url', 'description', 'genre']
	#template_name = 'musicplayer/channel_create.html'
	success_url = reverse_lazy('player_index')

	def form_valid(self, form):
		"""
		Overrides the saving-procedure of the Generic Views for own purposes.
		Updates the MPC
		"""
		self.object = form.save()

		# update MPC
		helpers.createWebradioPlaylist()

		# makes sure, that the correct object is saved and not overwritten in the direct baseclass
		return super(ModelFormMixin, self).form_valid(form)


# delete channels if you are allowed
class ChannelDelete(DeleteView):
	"""
	View for deleting a specific channel.
	Redirects to the editoverview.
	"""
	model = Channel
	success_url = reverse_lazy('player_edit_radio')
	url = reverse_lazy('player_edit_radio')
	#context_object_name = 'channel'


# edit channels
class ChannelEdit(ListView):
	"""
	Gives an overview over all channels and depending on your permissions possibilities to change them.
	With full permissions you can update/change and delete channels.
	"""
	model = Channel
	#template_name = 'musicplayer/channel_edit.html'
	#context_object_name = 'channels'


################################################################################

# updating a channel
class AlbumUpdate(UpdateView):
	"""
	Creates the View for Updating a channel.
	It updates the MPC playlist aswell after saving the channel to the database.
	"""
	model = Album
	#fields = ['name', 'url', 'description', 'genre',]
	#template_name = 'musicplayer/channel_update.html'
	success_url = reverse_lazy('player_edit_album')
	url = reverse_lazy('player_edit_album')


# create channels
class AlbumCreate(CreateView):
	"""
	Creates a new Album.
	"""
	model = Album
	#template_name = 'musicplayer/channel_create.html'
	success_url = reverse_lazy('player_edit_album')


# delete channels if you are allowed
class AlbumDelete(DeleteView):
	"""
	View for deleting a specific album.
	Redirects to the editoverview.
	"""
	model = Album
	success_url = reverse_lazy('player_edit_album')
	url = reverse_lazy('player_edit_album')
	context_object_name = 'channel'


# edit channels
class AlbumEdit(ListView):
	"""
	Gives an overview over all channels and depending on your permissions possibilities to change them.
	With full permissions you can update/change and delete channels.
	"""
	model = Album
	#template_name = 'musicplayer/channel_edit.html'
	#context_object_name = 'a'

################################################################################

# updating a channel
class BandUpdate(UpdateView):
	"""
	Creates the View for Updating a channel.
	It updates the MPC playlist aswell after saving the channel to the database.
	"""
	model = Band
	#fields = ['name', 'url', 'description', 'genre',]
	#template_name = 'musicplayer/channel_update.html'
	success_url = reverse_lazy('player_edit_band')
	url = reverse_lazy('player_edit_band')


# create channels
class BandCreate(CreateView):
	"""
	Creates a new Channel. You are subscribed to it automatically.
	It updates the MPC playlist aswell after saving the channel to the database.
	"""
	model = Band
	#fields = ['name', 'url', 'description', 'genre']
	#template_name = 'musicplayer/channel_create.html'
	success_url = reverse_lazy('player_edit_band')


# delete channels if you are allowed
class BandDelete(DeleteView):
	"""
	View for deleting a specific channel.
	Redirects to the editoverview.
	"""
	model = Band
	success_url = reverse_lazy('player_edit_band')
	url = reverse_lazy('player_edit_band')
	#context_object_name = 'channel'


# edit channels
class BandEdit(ListView):
	"""
	Gives an overview over all channels and depending on your permissions possibilities to change them.
	With full permissions you can update/change and delete channels.
	"""
	model = Band
	#template_name = 'musicplayer/channel_edit.html'
	#context_object_name = 'channels'

################################################################################

# updating a channel
class TitleUpdate(UpdateView):
	"""
	Creates the View for Updating a channel.
	It updates the MPC playlist aswell after saving the channel to the database.
	"""
	model = Title
	#fields = ['name', 'url', 'description', 'genre',]
	#template_name = 'musicplayer/channel_update.html'
	success_url = reverse_lazy('player_edit_title')
	url = reverse_lazy('player_edit_title')

	def form_valid(self, form):
		"""
		Overrides the saving-procedure of the Generic Views for own purposes.
		Updates the MPC.
		"""
		helpers.updateSongDatabase()
		return super(ChannelUpdate, self).form_valid(form)


# create channels
class TitleCreate(CreateView):
	"""
	Creates a new Channel. You are subscribed to it automatically.
	It updates the MPC playlist aswell after saving the channel to the database.
	"""
	model = Title
	#fields = ['name', 'url', 'description', 'genre']
	#template_name = 'musicplayer/channel_create.html'
	success_url = reverse_lazy('player_edit_title')

	def form_valid(self, form):
		"""
		Overrides the saving-procedure of the Generic Views for own purposes.
		Updates the MPC
		"""
		self.object = form.save()

		# update MPC
		helpers.updateSongDatabase()

		# makes sure, that the correct object is saved and not overwritten in the direct baseclass
		return super(ModelFormMixin, self).form_valid(form)


# delete channels if you are allowed
class TitleDelete(DeleteView):
	"""
	View for deleting a specific channel.
	Redirects to the editoverview.
	"""
	model = Title
	success_url = reverse_lazy('player_edit_title')
	url = reverse_lazy('player_edit_title')
	#context_object_name = 'channel'


# edit channels
class TitleEdit(ListView):
	"""
	Gives an overview over all channels and depending on your permissions possibilities to change them.
	With full permissions you can update/change and delete channels.
	"""
	model = Title
	paginate_by = 20
	#template_name = 'musicplayer/channel_edit.html'
	#context_object_name = 'channels'


################################################################################

# updating a channel
class PlaylistUpdate(UpdateView):
	"""
	Creates the View for Updating a channel.
	It updates the MPC playlist aswell after saving the channel to the database.
	"""
	model = Playlist
	#fields = ['name', 'url', 'description', 'genre',]
	#template_name = 'musicplayer/channel_update.html'
	success_url = reverse_lazy('player_edit_playlist')
	url = reverse_lazy('player_edit_playlist')

	def form_valid(self, form):
		"""
		Overrides the saving-procedure of the Generic Views for own purposes.
		Updates the MPC.
		"""
		helpers.updateSongDatabase()
		return super(ChannelUpdate, self).form_valid(form)


# create channels
class PlaylistCreate(CreateView):
	"""
	Creates a new Channel. You are subscribed to it automatically.
	It updates the MPC playlist aswell after saving the channel to the database.
	"""
	model = Playlist
	#fields = ['name', 'url', 'description', 'genre']
	#template_name = 'musicplayer/channel_create.html'
	success_url = reverse_lazy('player_edit_playlist')

	def form_valid(self, form):
		"""
		Overrides the saving-procedure of the Generic Views for own purposes.
		Updates the MPC
		"""
		self.object = form.save()

		# update MPC
		helpers.updateSongDatabase()

		# makes sure, that the correct object is saved and not overwritten in the direct baseclass
		return super(ModelFormMixin, self).form_valid(form)


# delete channels if you are allowed
class PlaylistDelete(DeleteView):
	"""
	View for deleting a specific channel.
	Redirects to the editoverview.
	"""
	model = Playlist
	success_url = reverse_lazy('player_edit_playlist')
	url = reverse_lazy('player_edit_title')
	#context_object_name = 'channel'


# edit channels
class PlaylistEdit(ListView):
	"""
	Gives an overview over all channels and depending on your permissions possibilities to change them.
	With full permissions you can update/change and delete channels.
	"""
	model = Playlist
	#template_name = 'musicplayer/channel_edit.html'
	#context_object_name = 'channels'




################################################################################
# control views
################################################################################

# using ajax for the responses
from django.http import JsonResponse

def json_response(request, context = {}):
	#if(request.META.get('HTTP_REFERER')):
	#	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	#else:
	#	return HttpResponseRedirect(reverse('player_index'))
	
	return JsonResponse(context)


def getCurrentlyPlaying(request):
	return json_response(request, { "currently_playing" : helpers.getCurrentTitle() })


def playChannel(request, pk):
	"""
	Processes the webrequest for playing a channel. It maps the primary key to the playlist-position from MPC.
	Redirects to the site where you came from --> no change in the view.
	"""
	# make sure webradioplaylist ist loaded
	if helpers.createWebradioPlaylist():
		helpers.loadPlaylist(WEBRADIO_PLAYLIST_NAME)

	else:
		return HttpResponseForbidden()


	nr = helpers.getTitleNumber(get_object_or_404(Channel, pk=int(pk)).url)

	if nr < 0:
		raise Http404

	# programm on the raspi
	helpers.play(nr)

	return json_response(request)


def playTitle(request, pk, space):
	"""Plays titles from the local files. The space controls how the complete
	playlist is selected by the pk
	good values for space:
		'album' -> selects all titles from the album with pk == pk
		'title' -> selects only the title
		'band' -> selects all title from a band
		'playlist' -> select all titles from a playlist and plays them
	"""
	space = space.lower()

	if space == 'title':
		titles = Title.objects.filter(pk = int(pk))
		helpers.modeReplay('off')

	elif space == 'album':
		titles = Album.objects.get(pk = int(pk)).title_set.all()
		# make mpc play the whole playlist
		helpers.modeReplay('album')

	elif space == 'band':
		titles = Band.objects.get(pk = int(pk)).title_set.all()
		# make mpc play the whole playlist
		helpers.modeReplay('album')

	elif space == 'genre':
		# get all titles from a genre
		titles = Title.objects.filter(genre__icontains = genre)
		# make mpc play the whole playlist
		helpers.modeReplay('album')
		
	elif space == 'playlist':
		# get all titles from a playlist
		titles = Playlist.objects.get(pk = int(pk)).titles.all()
		# make mpc play the whole playlist
		helpers.modeReplay('album')

	else:
		raise Http404

	helpers.clearPlaylist()

	# add every title to the current mpc playlist
	for t in titles:
		helpers.addElementToPlaylist(t.filepath)

	# start playing
	helpers.play(1)

	return json_response(request)


def play(request):
	"""
	Resumes playing the previous music.
	Redirects to the site where you came from --> no change in the view.
	"""
	helpers.play()

	return json_response(request)


def stop(request):
	"""
	Stops playing the music. Doesn't reset anything on MPC.
	Redirects to the site where you came from --> no change in the view.
	"""
	helpers.stop()

	return json_response(request)


def next(request):
	"""Play the next title in the current playlist."""
	helpers.nextTitle()
	
	return json_response(request)
	

def previous(request):
	"""Plays the previous title in the playlist."""
	helpers.prevTitle()
	
	return json_response(request)


def playRandom(request, random):
	helpers.modeRandom(random)

	return json_response(request)


def shufflePlaylist(request):
	helpers.shufflePlaylist()

	return json_response(request)


def playRepeat(request, repeat):
	helpers.modeRepeat(repeat)

	return json_response(request)


def playMode(request, mode):
	helpers.modeReplay(mode)

	return json_response(request)


def nextTitle(request):
	helpers.nextTitle()

	return json_response(request)


def prevTitle(request):
	helpers.prevTitle()

	return json_response(request)



def increaseVolume(request):
	"""
	Changes the Volume from the PI +10
	Redirects to the site where you came from --> no change in the view.
	"""
	helpers.increaseVolume()
	return json_response(request)


def decreaseVolume(request):
	"""
	Changes the Volume from the PI -10
	Redirects to the site where you came from --> no change in the view.
	"""
	helpers.decreaseVolume()
	return json_response(request)


def setVolume(request, vol):
	"""Sets the playing volume to a value, fails silently."""
	helpers.setVolume(int(vol))

	return json_response(request)


def updateMPC(request):
	"""Updates the internal database from mpc, needed if some of the Data on
	the filesystem changed."""
	#filemanagement.createTitleDatabase()
	helpers.updateSongDatabase()

	return json_response(request)
