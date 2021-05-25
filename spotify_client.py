#token = 'BQAmpxOUCrphHjJn0u7B6iXaX5c-K3Rg7VWpr6QGJ18Euy2mekoadJoIQZ5pxtIPyRwjpjQg-4QPiL5OYVuL3Ms11tb7V_7u5UZcl3tm3eZmwpQTpwlUuBbDBTKFKiPqtawCi6fkETX94yBOcauSpF6ogQtChG6lc_hPXm0cyS3uAO-_EQxhiTy799KWSW7G7NmFXpbb-eE0Xm6O8XFOfjhASHib5hgzoElNW9RqIzlPQFOeDGM6FhkNNs214_jXAATINAl1cIy3147AAX7GsqgTatcIxa_ple7Pqvv5'
import requests
import urllib.parse

class SpotifyClient(object):

    def __init__(self, api_token) -> None:
        self.api_token = api_token

    def serach_song(self, artist, track):
        query = urllib.parse.quote(f'{artist} {track}')
        url = f"https://api.spotify.com/v1/seach?q={query}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type" : "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        response_json = response.json()

        results = response_json['tracks']['items']

        if results:
            return results[0]['id']
        else:
            raise Exception(f"No song found for {artist} = {track}")



    def add_song_to_spotify(self, song_id):
        url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(
            url,
            json={
                "ids": [song_id]
            },
            headers={
                "Content-Type" : "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        return response.ok
