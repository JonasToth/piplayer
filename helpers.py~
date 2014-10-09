#!/usr/bin/env python
#-*- coding:utf-8 -*-

import subprocess
from subprocess import call, check_output
import time
import os

from musicplayer.settings import WEBRADIO_PLAYLIST_NAME, MPC_PLAYLIST_DIR, MPC_MUSIC_DIR
#from musicplayer.settings import VOLUME_DELTA


# ---------------------------------------------------------------------

def modeReplay(mode = 'off'):
	"""Specifies the Replaygain of mpc.

	available modes:
	off 	-- plays only the song once
	track 	-- plays the song in a loop
	album 	-- plays the complete playlist
	"""

	if mode in ('off', 'track', 'album'):
		call(["mpc", "replaygain", mode])
		return True

	else:
		return False


def modeRandom(random = True):
	"""Specifies to play the playlist in random order."""
	if random:
		call(["mpc", "random", "on"])
	else:
		call(["mpc", "random", "off"])

	return True


def modeRepeat(repeat = False):
	"""Specifies to repeat the Song."""
	if repeat:
		call(["mpc", "repeat", "on"])
	else:
		call(["mpc", "repeat", "off"])

	return True



#----------------------------------------------------------------------

def updateSongDatabase():
	"""Updates the mpd songdatabase"""
	call(["sudo", "service", "mpd", "restart"])
	call(["mpc", "update"])

	return True


def addElementToPlaylist(filepath):
	"""Adds a file/stream or whatever mpd can play to the current playlist."""
	call(["mpc", "add", filepath])


def loadPlaylist(playlist):
	"""Loads a playlist into the playing queue."""
	call(["mpc", "clear"])
	call(["mpc", "load", playlist])


def clearPlaylist():
	"""Clears the current mpc playlist for new loading of a playlist."""
	call(["mpc", "clear"])


def shufflePlaylist():
	"""Shuffles the playlist."""
	call(["mpc", "shuffle"])

	return True


def getPlaylist():
	"""Returns a list of title in the current playlist."""
	pls = check_output(["mpc", "playlist"])

	# creates a list with the lines as elements
	return tuple(pls.splitlines())


def createMPCPlaylist(item_list, name):
	"""
	Creates a Playlist for MPC from a given item-list.
	The item-list has to consist from strings, which are written raw in the
	playlist-file, for webradio, its the url, for local music, its the filepath
	to the songfile.
	"""
	try:
		p = os.path.join(MPC_PLAYLIST_DIR, name)
		f = open(p, "w+")

		for nr, item in enumerate(item_list):
			# write the line in the file
			f.write("%s\n" % item)

		return True

	except IOError as e:
		return False



def createWebradioPlaylist():
	from musicplayer.models import Channel

	channel_list = Channel.objects.all()

	item_list = []

	for c in channel_list:
		item_list.append(c.url)

	return createMPCPlaylist(item_list, WEBRADIO_PLAYLIST_NAME)


# --------------------------------------------------------------------


def increaseVolume():
	"""Increases the Volume of mpc."""
	call(["mpc", "volume", "+"])

	return True


def decreaseVolume():
	"""Decreases the Volume of mpc."""
	call(["mpc", "volume", "-"])

	return True


def setVolume(value):
	"""Sets the Volume of mpc to a given value.
	The Value has to be between 0 and 100."""
	if type(value) != int or value < 0 or value > 100:
		return False
	else:
		call(["mpc", "volume", str(value)])

		return True


def play(number = None):
	"""Plays the current choosen file."""
	if number is None:
		res = call(["mpc", "play"])
	else:
		return playTitle(number)

	return True


def playTitle(number):
	"""Plays the Title number <number> in the Playlist. 1 based!."""
	# erzeugt ein tuple aus den einzelnen zeilen der playlist und nimmt die laenge davon
	size = len(tuple(check_output(["mpc", "playlist"]).splitlines()))

	if type(number) is not int or (number > size or number < 1):
		return False

	else:
		call(["mpc", "play", str(number)])

		return True


def stop():
	"""Stops playing."""
	call(["mpc", "stop"])

	return True


def toggle():
	"""Toggles between playing and pausing. If stop was called, it acts like play()"""
	call(["mpc", "toggle"])

	return True


def nextTitle():
	"""Goes to the next title."""
	call(["mpc", "next"])

	return True


def prevTitle():
	"""Plays the previous file."""
	call(["mpc", "prev"])

	return True


# ---------------------------------------------------------------------

"""How a Status is represented:

	status = {
		"name" : --> channel name for radio / album name
		"band" : bandname of the song
		"title" : title currently playing
	}"""

def getPlayerStatus():
	"""TODO: Gibt ein Dictionary mit dem Aktuellen Status von mpd aus."""
	return None


def getPlaylistStatus(statusString = None):
	"""Gibt die Informationen wie man in der Aktuellen Playlist liegt in einem
	Dictionary zurück."""
	return None


def getMusicplayerStatus(statusString = None):
	"""Gives the informations about the currently played musicfile."""

	return None


def getWebradioStatus(statusString = None, titleFormat = r"([a-zA-Z0-9 ]+) - ([a-zA-Z0-9 ]+)"):
	"""TODO: gibt ein Dictionary mit dem Aktuellen Sender und dem Liedtitel aus.
	Dazu kommen noch die Statusdaten wie Lautstärke etc. siehe getStatus().

	Das Titelformat passt zu Rockantenne Heavy Metal.
	"""
	if statusString is None:
		try:
			p = subprocess.Popen("mpc status -f '%name% > %title%'", shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
			out = p.stdout.readlines()

		except subprocess.CalledProcessError as e:
			out = e.output

		#print "Output\n", out
		#print "Endoutput"

		try:
			radio, playlist, settings = out
		except ValueError:
			radio = ""
			playlist = ""
			settings = ""

	else:
		radio = statusString

	try:
		name, info = radio.split(">")
	except ValueError:
		name = None
		info = ""

	import re

	try:
		r = re.compile(titleFormat)
		try:
			#artist, title = r.split(info.strip())
			res = r.match(info.strip())
			#print res
			# ignore the empty matches from the regular expression

			artist, title = res.groups()
		except ValueError:
			artist = title = "Error while unpacking"
		except AttributeError:
			artist = title = "Regular expression not matching."

	except re.error:
		artist = title = "Error while matching"

	status = {}

	status["name"]	= name
	status["band"]	= artist
	status["title"]	= title

	return status


def getCurrentTitle():
	"""Gibt den aktuell gespielten Titel aus."""
	return check_output(["mpc", "current"])


def getTitleNumber(title):
	"""Gets the title number in the current playlist from the wanted title.
	If the title is not in the playlist, it returns -1."""
	pls = tuple(check_output(["mpc", "playlist"]).splitlines())

	try:
		# the playlist is 1 based, so convert it from 0 based tupleindizes
		return pls.index(title) + 1

	except ValueError:
		# element not in the playlist
		return -1

if __name__ == "__main__":
	loadPlaylist("sender")
	play(1)
	time.sleep(1)

	s = getWebradioStatus()

	print s["name"]
	print s["band"]
	print s["title"]
