import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Set up authentication
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope=scope
))

# Read songs from the text file
songs_file_path = os.getenv("FILE_PATH")
with open(songs_file_path, "r") as file:
    songs = [line.strip() for line in file if line.strip()]

# Prompt user for playlist name and description
playlist_name = input("Enter playlist name: ")
playlist_description = input("Enter playlist description: ")

# Create a new playlist
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user_id, playlist_name, public=True, description=playlist_description)

# Search for the tracks and add them to the playlist
track_uris = []
for song in songs:
    result = sp.search(q=song, limit=1)
    if result['tracks']['items']:
        track_uris.append(result['tracks']['items'][0]['uri'])

sp.playlist_add_items(playlist['id'], track_uris)
