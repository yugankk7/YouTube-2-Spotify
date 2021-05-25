import os
from spotify_client import SpotifyClient
from youtube_client import YoutubeClient

#put your token below
token = ''

def run():
    fpath = os.path.join('D:\PythonProjects\spot\creds', "client_secret.json")
    youtube_client = YoutubeClient(fpath)
    spotify_client = SpotifyClient(token)
    playlists = youtube_client.get_playlist()

    for index, playlist in enumerate(playlists):
        print(f"{index} : {playlist.title}")
    choice = int(input("Enter your choice..."))
    chosen_playlist = playlists[choice]
    print(f"You chose {chosen_playlist.title}")


    songs = youtube_client.get_video_from_playlist(chosen_playlist.id)
    print(f"Attempting to add {len(songs)} songs...")


    for song in songs:
        spotify_song_id = spotify_client.serach_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)

            if added_song:
                print(f"Added {song.artist}")



if __name__ == "__main__":
    run()
