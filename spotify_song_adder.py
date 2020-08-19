'''
	File Name: spotify_song_adder.py
	Author: Jason Nguyen
	Date Created: 27 May 2020
	Date Last Modified: 13 August 2020
	Python version 3.8

'''

# Generic / Built In
import os

# Downloaded
import spotipy.util as util
import spotipy


def init_connection(Client_ID, Client_Secret, Username, Redirect_URL):

	scope = 'playlist-modify-private'

	init_cmd = ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI"]
	init_cmd_imputs = [Client_ID, Client_Secret, Redirect_URL]
	for i in range(0,len(init_cmd)):
		os.environ[init_cmd[i]] = init_cmd_imputs[i]

	token = util.prompt_for_user_token(Username, scope)

	sp = spotipy.Spotify(auth=token)

	return sp

def add_song_to_playlist(sp, username, Playlist_ID, song_id): 

	sp.trace = False
	response = sp.playlist_tracks(Playlist_ID, offset=0, fields='items.track.id,total')

	song_ida = [song_id]

	song = sp.track(song_id)

	song_uri = song['uri'].split(':')[-1]

	offset = 0
	# ~ #checks if song is in playlist
	while len(response['items']) != 0:
		for i in response['items']:
			if i['track']['id'] == song_uri:
				return 'Song ({}) already in playlist ({})'.format(sp.track(song_id)['name'], sp.user_playlist(username, Playlist_ID)['name'])
		offset += 100
		response = sp.playlist_tracks(Playlist_ID, offset=offset, fields='items.track.id,total')

	results = sp.user_playlist_add_tracks(username, Playlist_ID, [song_id], position = 0)

	song_name = sp.track(song_id)['name']
	song_artist = song_artist = sp.track(song_id)['artists'][0]['name']
	return 'Added song: {} by {}'.format(song_name, song_artist)
		
