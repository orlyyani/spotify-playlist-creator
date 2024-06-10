
# Spotify Playlist Creator

This Python script allows you to create a Spotify playlist based on a list of songs provided in a text file.

## Features

- Reads a list of songs from a text file.
- Prompts the user to input the playlist name and description.
- Handles authentication with the Spotify API using environment variables.
- Adds the searched tracks to the created playlist.

## Usage

1. Prepare a text file containing a list of songs, with each song on a separate line.
2. Run the Python script.
3. Follow the prompts to input the playlist name and description.
4. The script will search for each song on Spotify and add them to the created playlist.

## Requirements

- Python 3.x
- Python-dotenv
- Spotipy

## Getting Started

1. Clone this repository.
2. Install the required dependencies:

    ```bash
    pip install python-dotenv spotipy
    ```

3. Set up your Spotify Developer account and obtain client ID, client secret, and redirect URI.
4. Create a `.env` file in the project directory and add your Spotify credentials:

    ```
    SPOTIPY_CLIENT_ID=your_client_id
    SPOTIPY_CLIENT_SECRET=your_client_secret
    SPOTIPY_REDIRECT_URI=your_redirect_uri
    ```

5. Prepare a text file with the list of songs you want to add to the playlist.
6. Run the Python script:

    ```bash
    python spotify_playlist_creator.py
    ```

7. Follow the prompts to input the playlist name and description.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
