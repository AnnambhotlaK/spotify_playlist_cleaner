import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = '42ebfded09144122aa0f0906eb853930',
                                                      client_secret = 'ef3261454aef4d6c84b9d67543e7a927',
                                                      user = 'K4Annam'))

playlists = spotify.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = spotify.next(playlists)
    else:
        playlists = None