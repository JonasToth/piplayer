#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from musicplayer.views import *
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = patterns('musicplayer.views',
	# play song/channel in the current playlist
    url(r'^playRadio/(?P<pk>\d+)/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playChannel)),
    	name = 'play_channel'),

    url(r'^playTitle/(?P<pk>\d+)/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playTitle)),
    	{ 'space' : 'title' }, name = 'play_title'),


    url(r'^playAlbum/(?P<pk>\d+)/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playTitle)),
    	{ 'space' : 'album' }, name = 'play_album'),


    url(r'^playBand/(?P<pk>\d+)/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playTitle)),
    	{ 'space' : 'band' }, name = 'play_band'),

    url(r'^playGenre/(?P<genre>\w+)/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playTitle)),
    	{ 'space' : 'genre' }, name = 'play_genre'),
    	
    url(r'^playPlaylist/(?P<pk>\w+)/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playTitle)),
    	{ 'space' : 'playlist' }, name = 'play_playlist'),


   	# play again previous played channel
   	# resumes playing
    url(r'^play/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(play)),
    	name = 'continue_playing'),


	# stops playing musicplayer
    url(r'^stop/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(stop)),
    	name = 'stop_playing'),
    	
    
    # play the next title in the playlist
    url(r'^next/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(next)),
    	name = 'next_title'),
    	
    # play the previous title in the playlist
    url(r'^previous/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(previous)),
    	name = 'previous_title'),

    # increase volume
    url(r'^incVol/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(increaseVolume)),
    	name = 'increase_volume'),


    # decrease volume
    url(r'^decVol/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(decreaseVolume)),
    	name = 'decrease_volume'),

    # decrease volume
    url(r'^vol/(\d+)/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(setVolume)),
    	name = 'set_volume'),

    # set the playing mode to random
    url(r'^playRandom/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playRandom)),
    	{ 'random' : True }, name = 'play_random'),

    # set the playing mode to not random
    url(r'^stopRandom/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playRandom)),
    	{ 'random' : False }, name = 'play_random'),

    # shuffle the current playlist, only usefull for local files
    url(r'^shufflePlaylist/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(shufflePlaylist)),
    	name = 'shuffle_playlist'),

    # repeats the current file always
    url(r'^playRepeat/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playRepeat)),
    	{'repeat' : True }, name = 'play_repeat'),

    # stops repeating the current file
    url(r'^stopRepeat/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playRepeat)),
    	{'repeat' : False }, name = 'play_repeat'),


    # controls how the playlist is treated

    # replays the complete list
    url(r'^playMode/(?P<mode>album)/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playMode)),
		name = 'play_mode_album'),
    # replays the current track
    url(r'^playMode/(?P<mode>track)/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playMode)),
    	name = 'play_mode_track'),
    # plays only on file and ends afterwards
    url(r'^playMode/(?P<mode>off)/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(playMode)),
    	name = 'play_mode_off'),


    # update the mpc database for propper working
    # needed if new titles are in the filesystem or the title have changed in
    # the filesystem
    url(r'^updateMPC/$',
    	permission_required('musicplayer.can_control', raise_exception = True)(login_required(updateMPC)),
    	name = 'update_mpc'),


	# gets the title that currently played
	# called as ajax, response is only json
	url(r'^getCurrentlyPlaying/$',
		permission_required('musicplayer.can_control', raise_exception = True)(login_required(getCurrentlyPlaying)),
    	name = 'get_currently_playing'),

)
