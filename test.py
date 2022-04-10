import math
import base64
from secrets import *
import requests
import urllib.parse
import time
import serial

# Certification
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_GET_PLAYBACK_STATE_URL = 'https://api.spotify.com/v1/me/player'
SPOTIFY_ACCESS_TOKEN = 'BQBdfE_02ZWFH7OFmxRbK1UXsgJjrgpR9rNNDL7i4N01zfLGYBZ6vJ9gRif-0lsjGzQ1bKHl8ywVf5ffw1OEsrGVhSmnh96F_TA-MyFWfs-sCCjpeR_ZM_rzFZaEHQ2ckTxTTJLcUhJ_LeycaDSrJpSKbg'
GET_LYRICS_URL = 'https://api.textyl.co/api/lyrics?q='
ARD = serial.Serial("COM3", 9600)

# We're going to give it the access token and get back the data we need
# Then we have to process that data, since it is in a format that we're going to need to make it more "friendly"
def get_current_track(access_token):
    # Stores the result of calling the Spotify API in JSON format -- Using the request library
    # Type of request: get request -- Params:
    #       URL: Will call out to a URL
    #       Headers: Takes in a dictionary
    try:
        response = requests.get(
            SPOTIFY_GET_CURRENT_TRACK_URL,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        response.raise_for_status()

        # Response JSON -- Whenever you take an API call using the request library,
        # it gives you back a response object, which is the JSON response (A Python
        # Dictionary that makes things easier to work with).
        resp_json = response.json()

        # Process Response JSON -- all from Spotify's response dictionary
        progress = resp_json['progress_ms'] / 1000.0
        duration = resp_json['item']['duration_ms'] / 1000.0
        track_id = resp_json['item']['id']
        track_name = resp_json['item']['name']
        artists = resp_json['item']['artists']  # This is an array of artists
        # Takes an array of artist names, and join them with the ', ' string
        artist_names = ', '.join(
            [artist['name'] for artist in artists]
        )

        return track_name + ' ' + artist_names, progress, duration
    except requests.exceptions.HTTPError:
        print('Error get_current_track caught')
        return None, 0.0


def is_playing(access_token):
    try:
        r = requests.get(
            SPOTIFY_GET_PLAYBACK_STATE_URL,
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )
        print(r.raise_for_status())

        return r.json()['is_playing']
    except requests.exceptions.HTTPError:
        print('Error is_playing caught')
        return False

def get_lyrics(title):
    song_url = urllib.parse.quote(title)
    lyric_url = GET_LYRICS_URL + song_url
    lyrics = requests.get(lyric_url).json()
    return lyrics

def print_lyrics(lyrics, progress, duration):
    progress_duration = progress
    last_time = time.time()
    total_lines = len(lyrics)  # total lyric lines
    line_i = 0  # current line index
    prev = -1 # previous line index

    while line_i < total_lines:  # keep on going until no more lyrics to display
        line = lyrics[line_i]  # current line
        sec = line['seconds']  # current sec
        lyr = line['lyrics']  # current lyric

        if line_i < total_lines - 1:
            next_line = lyrics[line_i + 1]  # next in the dict
            next_sec = next_line['seconds']  # next second in the dict

        if line_i != prev:
            # print in console and to arduino
            print(lyr)
            ARD.write(str(lyrics))
            prev = line_i

        if progress + (time.time() - last_time) >= next_sec - 0.5:
            line_i += 1

    progress_duration += time.time() - last_time

    time.sleep(duration - progress_duration)

    return True

def main():
    pressed = 1

    while pressed == 1:
        pressed = ARD.read()

    song_ended = True

    while song_ended == True:
        song_ended = False
        # Get current track of user
        # track-artist name, start progress
        res = get_current_track(SPOTIFY_ACCESS_TOKEN)
        print(res)
        curr_track_info, start_progress, duration = get_current_track(SPOTIFY_ACCESS_TOKEN)

        print(curr_track_info)

        # Get Lyrics of track-artist
        lyrics = get_lyrics(curr_track_info)

        # Print Lyrics
        if is_playing(SPOTIFY_ACCESS_TOKEN):
            song_ended = print_lyrics(lyrics, start_progress, duration)

if __name__ == '__main__':
    main()
