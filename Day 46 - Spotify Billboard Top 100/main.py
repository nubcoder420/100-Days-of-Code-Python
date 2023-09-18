from pprint import pprint

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

SPOTIFY_CLIENT_ID = "YOUR CLIENT ID HERE"
SPOTIFY_CLIENT_SECRET = "YOU CLIENT SECRET HERE"
SPOTIFY_REDIRECT_URI = "http://example.com"
SPOTIFY_SCOPE = "playlist-modify-private"
SPOTIFY_CACHE_PATH = "token.txt"

BILLBOARD_SITE = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
site = f"{BILLBOARD_SITE}{date}/"

response = requests.get(url=site)
top_100_page = response.text


soup = BeautifulSoup(top_100_page, "html.parser")

billboard_top_100 = []
title_list = []

for chart_result in soup.find_all("ul", class_="o-chart-results-list-row"):
    song_title = chart_result.h3.text.strip()
    song_artist = chart_result.h3.next_sibling.next_sibling.text.strip()

    # print(song_title)
    # print(song_artist)
    # print()
    new_data = {
        "title": song_title,
        "artist": song_artist,
    }
    billboard_top_100.append(new_data)
    title_list.append(song_title)

# pprint(billboard_top_100)
# pprint(title_list)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        # cache_path=SPOTIFY_CACHE_PATH,
    )
)
user_id = sp.current_user()["id"]
print(user_id)

year = date.split("-")[0]
song_uris = []

for title in title_list:
    result = sp.search(q=f"track: {title} year: {year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{year} Billboard Top 100",
    public=False,
)

print(playlist)

sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)
