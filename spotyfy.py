import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_songs():
    id = input('enter client id: ')
    secret = input('enter client secret: ')
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= id,
                                                client_secret= secret,
                                                redirect_uri='http://localhost:5000/callback',
                                                scope='playlist-read-private'))

    playlist_id = input('enter playlist id: ')
    playlist = sp.playlist(playlist_id)

    track_info = [(track['track']['name'], ', '.join([artist['name'] for artist in track['track']['artists']])) for track in playlist['tracks']['items']]

    file_name = 'songs.txt'

    with open(file_name, 'w') as file:
        pass
        
    with open(file_name, 'w') as file:
        for song, artist in track_info:
            file.write(f'{artist} - {song}\n')

    print(f'Successfully saved track information to {file_name}')

get_songs()



