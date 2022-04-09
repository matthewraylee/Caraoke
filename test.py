import requests
import time
from pprint import pprint
import urllib.parse

# Certification
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player'
SPOTIFY_ACCESS_TOKEN = 'BQBidmoshmrh9XcBVgmzjH_3wyKTkiqp9nOYNvGmEXkc66PSWV47s33bTnuXVuJ9qSYLUAQLOlyBn51BaeMYXtQX-' \
                       'VdzbOJR8D4yyHDfjqNe599jjyMUEQnEc11KDr9FpTBmTYK0bOCIU7bEDc2bq_vx6qe0Rhh6_ezMswKy1-VqnWE'

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
    # Link to the song
    link = resp_json['item']['external_urls']['spotify']

    # The dictionary we want to return
    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists": artist_names,
        "link": link
    }

    return current_track_info


# def getLyrics(title):

def main():
    while True:
        current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)

        # Pretty Print - Nice way of printing out dictionaries
        pprint(current_track_info, indent=4)

        # Let it run every 2 seconds
        time.sleep(2)


if __name__ == '__main__':
    main()
