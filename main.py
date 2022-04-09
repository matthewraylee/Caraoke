import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                               redirect_uri=cred.redirect_url, scope=scope))

results = sp.current_user_recently_played()
# track = sp.current_user_playing_track()
# print(json.dumps(track, sort_keys=True, indent=4))
# print()
# artist = track['item']['artists'][0]['name']
# track = track['item']['name']
#
# if artist !="":
#     print("Currently playing " + artist + " - " + track)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

