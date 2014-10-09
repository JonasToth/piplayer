#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url, include
from django.views.generic.edit import UpdateView

from musicplayer.views import *
from django.contrib.auth.decorators import login_required, permission_required

"""
	URLconf für musicplayer app
"""

urlpatterns = patterns('musicplayer.views',
	# startseite
	# controll it, have an overview
	url(r'^$',
		permission_required('musicplayer.can_view', raise_exception = True)(login_required(playerIndex)),
		name = 'player_index'),


	# create a channel, updates the mpc as well
	url(r'^createRadio/$',
		permission_required('musicplayer.add_channel', raise_exception = True)(login_required(ChannelCreate.as_view())),
		name = 'player_create_radio'),


	# editing overview to all channels available!
	url(r'^editRadio/$',
		permission_required('musicplayer.change_channel', raise_exception = True)(login_required(ChannelEdit.as_view())),
		name = 'player_edit_radio'),


	# update a specific channel
	# called from edit_channels
	url(r'^editRadio/(?P<pk>\d+)/$',
		permission_required('musicplayer.change_channel', raise_exception = True)(login_required(ChannelUpdate.as_view())),
		name = 'player_update_radio'),



	# deletes a specific channel
	# called from edit_channels
	url('^deleteRadio/(?P<pk>\d+)/$',
		permission_required('musicplayer.delete_channel', raise_exception = True)(login_required(ChannelDelete.as_view())),
		name = 'player_delete_radio'),


	# create a album
	url(r'^createAlbum/$',
		permission_required('musicplayer.add_album', raise_exception = True)(login_required(AlbumCreate.as_view())),
		name = 'player_create_album'),


	# editing album
	url(r'^editAlbum/$',
		permission_required('musicplayer.change_album', raise_exception = True)(login_required(AlbumEdit.as_view())),
		name = 'player_edit_album'),


	# update a specific album
	# called from player_edit_album
	url(r'^editAlbum/(?P<pk>\d+)/$',
		permission_required('musicplayer.change_album', raise_exception = True)(login_required(AlbumUpdate.as_view())),
		name = 'player_update_album'),


	# deletes a specific album
	# called from player_edit_album
	url('^deleteAlbum/(?P<pk>\d+)/$',
		permission_required('musicplayer.delete_album', raise_exception = True)(login_required(AlbumDelete.as_view())),
		name = 'player_delete_album'),



	# create a band
	url(r'^createBand/$',
		permission_required('musicplayer.add_band', raise_exception = True)(login_required(BandCreate.as_view())),
		name = 'player_create_band'),


	# editing overview to all bands available!
	url(r'^editBand/$',
		permission_required('musicplayer.change_band', raise_exception = True)(login_required(BandEdit.as_view())),
		name = 'player_edit_band'),


	# update a specific band
	# called from player_edit_band
	url(r'^editBand/(?P<pk>\d+)/$',
		permission_required('musicplayer.change_band', raise_exception = True)(login_required(BandUpdate.as_view())),
		name = 'player_update_band'),


	# deletes a specific band
	# called from player_edit_band
	url('^deleteBand/(?P<pk>\d+)/$',
		permission_required('musicplayer.delete_band', raise_exception = True)(login_required(BandDelete.as_view())),
		name = 'player_delete_band'),



	# create a title, updates the mpc as well
	url(r'^createTitle/$',
		permission_required('musicplayer.add_title', raise_exception = True)(login_required(TitleCreate.as_view())),
		name = 'player_create_title'),


	# editing overview to all titles available!
	url(r'^editTitle/$',
		permission_required('musicplayer.change_title', raise_exception = True)(login_required(TitleEdit.as_view())),
		name = 'player_edit_title'),


	# update a specific title
	# called from player_edit_title
	url(r'^editTitle/(?P<pk>\d+)/$',
		permission_required('musicplayer.change_title', raise_exception = True)(login_required(TitleUpdate.as_view())),
		name = 'player_update_title'),



	# deletes a specific title from the database, not the filesystem!
	# called from player_edit_title
	url('^deleteTitel/(?P<pk>\d+)/$',
		permission_required('musicplayer.delete_title', raise_exception = True)(login_required(TitleDelete.as_view())),
		name = 'player_delete_title'),


	# create a title, updates the mpc as well
	url(r'^createPlaylist/$',
		permission_required('musicplayer.add_playlist', raise_exception = True)(login_required(PlaylistCreate.as_view())),
		name = 'player_create_playlist'),


	# editing overview to all titles available!
	url(r'^editPlaylist/$',
		permission_required('musicplayer.change_playlist', raise_exception = True)(login_required(PlaylistEdit.as_view())),
		name = 'player_edit_playlist'),


	# update a specific title
	# called from player_edit_title
	url(r'^editPlaylist/(?P<pk>\d+)/$',
		permission_required('musicplayer.change_playlist', raise_exception = True)(login_required(PlaylistUpdate.as_view())),
		name = 'player_update_playlist'),



	# deletes a specific title from the database, not the filesystem!
	# called from player_edit_title
	url('^deletePlaylist/(?P<pk>\d+)/$',
		permission_required('musicplayer.delete_playlist', raise_exception = True)(login_required(PlaylistDelete.as_view())),
		name = 'player_delete_playlist'),




	# calls the control urls
	url('^control/', include('musicplayer.control_urls')),
)
