import math

import requests
import urllib.parse
import time

# Certification
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = 'BQDN-xm2xPJwzLsumPnA6GBEg2ybtOTt4BDLTbVM1SAckYvwo2M3AkjHwm1hPFMcNMuTm6cynq7IhC_o-0LRGc6mVIp_PDT6r5dLc4pofKLO5p_INFKj5nX8NeySpBxJp53D9fGmukLIYLxJwyC0AzZoKnsOwXI0QAOJW8qvLNs'

GET_LYRICS_URL = 'https://api.textyl.co/api/lyrics?q='


# Issue out a request to the spotify API
# We're going to give it the access token and get back the data we need
# Then we have to process that data, since it is in a format that we're going to need to make it more "friendly"
def get_current_track(access_token):
    # Stores the result of calling the Spotify API in JSON format -- Using the request library
    # Type of request: get request -- Params:
    #       URL: Will call out to a URL
    #       Headers: Takes in a dictionary
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    # Response JSON -- Whenever you make an API call using the request library,
    # it gives you back a response object, which is the JSON response (A Python
    # Dictionary that makes things easier to work with).
    resp_json = response.json()

    # Process Response JSON -- all from Spotify's response dictionary
    track_id = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']  # This is an array of artists
    # Takes an array of artist names, and join them with the ', ' string
    artist_names = ', '.join(
        [artist['name'] for artist in artists]
    )

    return track_name + ' ' + artist_names, duration


# def getLyrics(title):

def main():
    curr_track_info, progress = get_current_track(SPOTIFY_ACCESS_TOKEN)

    lyrics = get_lyrics(curr_track_info)

    # Print Lyrics
    print_lyrics(lyrics, progress)


def get_lyrics(title):
    song_url = urllib.parse.quote(title)
    # print(song_url)
    lyric_url = GET_LYRICS_URL + song_url
    lyrics = requests.get(lyric_url).json()
    # print(lyrics.json())
    return lyrics


def print_lyrics(lyrics, progress):
    last_time = time.time()
    total_lines = len(lyrics)  # total lyric lines
    line_i = 0  # current line index
    prev = -1

    while line_i < total_lines:  # keep on going until no more lyrics to display
        line = lyrics[line_i]  # current line
        sec = line['seconds']  # current sec
        lyr = line['lyrics']  # current lyric

        if line_i < total_lines - 1:
            next_line = lyrics[line_i + 1]  # next in the dict
            next_sec = next_line['seconds']  # next second in the dict

        if line_i != prev:
            print(lyr)
            prev = line_i

        if progress + (time.time() - last_time) >= next_sec:
            line_i += 1

if __name__ == '__main__':
    main()
