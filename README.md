# GroupMe-Spotify-Chatbot
Grabs Spotify links from a GroupMe chat and adds them to a collective Spotify Playlist.

## Installation

Download the folder containing the following files:
* groupme_listener.py
* run_bot.py
* spotify_song_adder.py
* input_info.txt

You will need to install the following modules:
* [GroupyAPI](https://groupy.readthedocs.io/en/latest/index.html#)
* [Spotipy](https://spotipy.readthedocs.io/en/2.13.0/#)

## Usage
Input all of the correct and necessary information in the input_info.txt file. You will need to have opened up an app and received the token information from both GroupMe and Spotify. Once you have all of the correct information input into the file, run the run_bot.py file like so:

```python
python3 run_bot.py
```
Spotify may attempt to verify your login if you are doing it for the first time.

Running __run_bot.py__ the first time will create a log file that stores the last GroupMe message ID that you have checked. 

__groupme_listener.py__ will grab every spotify link that has been sent in the groupme chat and return a list of spotify links. If it has not logged a message ID before, it will grab every spotify link since the creation of the group. If it has logged a message ID, it will grab every link in the all of the messages since the last checked ID. 

__spotify_song_adder.py__ takes those links and searches your playlist for that song, if it is not already present in the playlist, it will add it to the playlist.

I have the run_bot.py file running on a cronjob on my raspi although you are welcome to run it occasionally and will work either way.

## Contributing
Please open an issue to discuss any changes that you would like for me to add.

## License
[MIT](https://choosealicense.com/licenses/mit/)
