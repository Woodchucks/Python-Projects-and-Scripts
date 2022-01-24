import os
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import json

URL = "https://www.billboard.com/charts/hot-100"

date = input("Pick a year to listen to music from the past. Type the date in format YYY-MM-DD:\n")

response = requests.get(f"{URL}/{date}/")
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")

titles_in_li = soup.select(selector="li h3", class_="o-chart-results-list__item")
titles_in_li_list = [title.getText().split("\n")[1] for title in titles_in_li]

with open("the_hot_100.txt", "w", encoding="utf8") as file:
    for title in titles_in_li_list:
        file.write(title + "\n")

# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=os.environ['SPOTIPY_CLIENT_ID'],
#         client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )

scope = 'playlist-modify-public'
username = os.environ['SPOTIFY_USERNAME']

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)

#create the playlist
playlist_name = input("Enter a playlist name:\n")
playlist_description = input("Enter the playlist description:\n")

spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)

list_of_songs = []
year = date.split("-")[0]
for title in titles_in_li_list:
    result = spotifyObject.search(q=f"{title} year:{year}",type="track")
    # print(json.dumps(result,sort_keys=4,indent=4))
    try:
        # print(result['tracks']['items'][0]['uri'])
        list_of_songs.append(result['tracks']['items'][0]['uri'])
    except:
        # print("The song was not found")
        pass

pre_playlist = spotifyObject.user_playlists(user=username)
playlist = pre_playlist['items'][0]['id']
spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_of_songs)
