'''
	File Name: run_bot.py
	Author: Jason Nguyen
	Date Created: 27 May 2020
	Date Last Modified: 13 August 2020
	Python version 3.8

'''

# Should be in same folder
import groupme_listener, spotify_song_adder

# Generic / Built In
import sys

# run function uses both the GroupMe listener and the 
# spotify song adder to find and add songs to the playlist
def run(groupme_info, spotify_info):

	list_of_songs = groupme_listener.grab_song_links(groupme_info['Token'], groupme_info['Group_Name'])

	if list_of_songs:

		sp = spotify_song_adder.init_connection(spotify_info['Client_ID'], spotify_info['Client_Secret'],
											    spotify_info['Username'], spotify_info['Redirect_URL'])

		for song in list_of_songs:

			print(spotify_song_adder.add_song_to_playlist(sp, spotify_info['Username'], spotify_info['Playlist_ID'], song))

# grab_info function grabs necessary info from the InputInfo.txt file
def grab_info():
	try:
		with open("input_info.txt") as file:
			f = [next(file) for x in range(7)]
	except:
		print("Missing file: input_info.txt")
		sys.exit()

	groupme_info = {}
	spotify_info = {}

	for i in f:

		label = i[0:i.find(" ")]
		info = i[i.find("(")+1:i.find(")")]

		if not info:

			print("Missing info in ", label)
			print("Add correct information into input_info.txt")

			return

		if not i.find("Spotify"):

			spotify_info[label[8:]] = info

		if not i.find("GroupMe"):

			groupme_info[label[8:]] = info

	return groupme_info, spotify_info

groupme_info, spotify_info = grab_info()

run(groupme_info, spotify_info)