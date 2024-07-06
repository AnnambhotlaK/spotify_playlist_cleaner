import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-recently-played"

SPOTIPY_CLIENT_ID = '42ebfded09144122aa0f0906eb853930'
SPOTIPY_CLIENT_SECRET = 'ef3261454aef4d6c84b9d67543e7a927'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = SPOTIPY_CLIENT_ID,
    client_secret = SPOTIPY_CLIENT_SECRET,
    redirect_uri = SPOTIPY_REDIRECT_URI,
    scope = scope,
    )
)

results = spotify.current_user_recently_played(limit = 50)

for index, item in enumerate(results['items']):
    track = item['track']
    print((index + 1), track['artists'][0]['name'], " – ", track['name'])