'''
	File Name: GroupMe_listener.py
	Author: Jason Nguyen
	Date Created: 27 May 2020
	Date Last Modified: 13 August 2020
	Python version 3.8

'''

# Downloaded
from groupy.client import Client
from groupy import session

# Generic / Built In
import time
import logging, csv, os, sys


def get_group_chat(client, GroupMe_Group_Name):

	group_chat = {}
	for group in client.groups.list():
		if group.name == "Rave Club's Playlist":
			group_chat = group
	return group_chat

# Get's last message ID, creates log file if one does not exist
def get_last_id():

	try:
		data = []
		f = open("log.txt", "r")
		f.read()

		return f

	except:
		filename = "log.txt"
		# opening the file with w+ mode truncates the file
		f = open(filename, "w+")
		f.close()

		logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(message)s')
		logging.info("none")

def grab_song_links(GroupMe_Token, GroupMe_Group_Name):

	# Authorization Step, Returns Client
	client = Client.from_token(GroupMe_Token)

	# Grabs Group Chat
	group_chat = get_group_chat(client, GroupMe_Group_Name)

	# Grabs last message ID from previous runs
	last_message = get_last_id()
	
	# Grabs list of messages after last message
	try:
		list_of_messages = list(group_chat.messages.list_after(last_message))
		
	#if there is no ID/not recognized, grabs every single message in the list
	except:
		list_of_messages = list(group_chat.messages.list().autopage())


	# Note: Groupy list() function always returns a page of messages even if you
	# include a since_id so spotify song adder will always have to check if the song
	# isn't added already. Spotify song adder will need that function anyways to
	# make sure that the song hasn't been added by someone before.
		
	# Initializes list of songs to add to spotify

	list_of_songs = []


	for message in list_of_messages:
		
		if message.text != None:

			x = message.text[message.text.find("https://open.spotify.com/track"):message.text.find(" ")]
			if x:
				list_of_songs.append(x)

	# Creates new log ID
	last_message = list_of_messages[0].id
	
	filename = "log.txt"
	# opening the file with w+ mode truncates the file
	f = open(filename, "w+")
	f.close()

	logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(message)s')
	logging.info(last_message)

	# Returns a reversed list as the list of messages is returned in reversed order. 
	# Reversing the final list ensures that the songs are added in the same order they were sent.

	list_of_songs.reverse()

	return list_of_songs
