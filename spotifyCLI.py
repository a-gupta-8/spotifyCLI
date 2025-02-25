import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import click

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = "user-library-read user-read-playback-state user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))


def get_track_uri(song_name, artist_name=None):
    results = sp.search(q=song_name, type='track', limit=1)  # Get the top result
    track = results['tracks']['items'][0]
    track_uri = track['uri']
    return track_uri


@click.command()
def play():
    player = sp.current_playback()
    track = player['item']
    song_name = track['name']
    artist = track['artists'][0]['name']
    click.echo(f"playing {song_name} by {artist}")
    sp.start_playback()

@click.command()
def pause():
    click.echo("paused")
    sp.pause_playback()

@click.command()
@click.argument("song_name")
def sing(song_name):
    track_uri = get_track_uri(song_name)
    click.echo("Okay.")
    sp.start_playback(uris=[track_uri])

@click.group()
def cli():
    pass

cli.add_command(play)
cli.add_command(pause)
cli.add_command(sing)

if __name__ == "__main__":
    cli()
