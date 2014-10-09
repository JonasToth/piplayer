#!/usr/bin/env python
#-*- coding:utf-8 -*-

from musicplayer.models import *
#from raspberrypi_control.push_to_pi import File
from musicplayer.settings import MPC_MUSIC_DIR
import os

class File(object):
	"""
	Class to abstract files for uploading to the Upload.
	This informations are used for the proper put command
	while uploading.
	"""
	def __init__(self, filepath):
		"""Saves the filepath and wheters its an directory"""
		self.__path = filepath if os.path.exists(filepath) else None
		self.__is_directory = os.path.isdir(filepath)

	def getPath(self):
		"""Returns the filepath as string or an empty string."""
		return self.__path if self.__path else ""

	def is_directory(self):
		"""True if the File is a directory."""
		return self.__is_directory

	def __repr__(self):
		"""Writes its Filepath or 'invalid path!' if the filepath does not exist."""
		if self.__path:
			return os.path.normcase(self.__path)
		return "invalid path!"


def createTitleDatabase():
	"""Creates the Title Database for all the files which are in the current
	musicdirectory relevant for mpc."""


	titles = findRelevantFilesRecursive(MPC_MUSIC_DIR)

	#for t in titles:
	#	print os.path.relpath(t.getPath(), MPC_MUSIC_DIR)

	for t in titles:
		tmp = Title(name = os.path.basename(t.getPath()), filepath = os.path.relpath(t.getPath(), MPC_MUSIC_DIR))
		tmp.save()



def findRelevantFilesRecursive(path):
	"""
	Searches all the Files who should be pushed to the Pi.
	This excludes settings and stuff you dont need on the Pi for
	a working site.

	Looking for:
		- Pictures(*.png, *.jpg, *.jpeg, *.gif)x
		- Python(*.py)x
		- HTML(*.html)x
		- CSS(*.css)x
		- JavaScript(*.js)x
	excludes explicitly:
		- settings.py everywhere
		- all generate files
		- push_to_pi.py
		- .git directory
	"""
	files = os.listdir(path)
	filelist = []

	# go through and append the right files
	for f in files:
		# get the correct filename with relativ path to the project
		f = os.path.join(path, f)

		# this one is a directory
		# go recursivly and ignore the git repo
		if os.path.isdir(f) and f != ".git":
			subdirectory = findRelevantFilesRecursive(f)

			# extend the filelist with the new found files
			filelist.extend(subdirectory)

		# check for relevanz
		else:
			name, extension = os.path.splitext(f)

			# crops the dot away from the file extension
			ext = extension[1:]

			# everything which is used anyway
			if ext == "mp3" or ext == "ogg":
				print "Relevant: ", f
				filelist.append(File(f))

	return filelist



def findRelevantFiles():
	"""
	Searches all the Files who should be in the Titledatabase. Has to be reworked

	Looking for:
		- Pictures(*.png, *.jpg, *.jpeg, *.gif)
		- Python(*.py)x
		- HTML(*.html)x
		- CSS(*.css)x
		- JavaScript(*.js)x
	excludes explicitly:
		- settings.py everywhere
		- all generate files
		- push_to_pi.py
		- .git directory
	"""
	# start in the projectstructure
	# this script has to be called from ~/raspberrypi_control
	filelist = findRelevantFilesRecursive(".")

	return filelist
