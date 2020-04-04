"""Example app to print the currently playing song periodically."""

import os
import time
import webbrowser
from datetime import datetime as dt

import spotifier.scopes as S
from spotifier import Spotify
from spotifier.oauth import SpotifyAuthorizationCode


def main():
    oauth = SpotifyAuthorizationCode(
        client_id=os.environ["SPOTIFY_CLIENT_ID"],
        client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
        redirect_uri=os.environ["SPOTIFY_REDIRECT_URI"],
        scopes=[S.USER_READ_CURRENTLY_PLAYING],
    )

    webbrowser.open(oauth.get_authorize_url())
    url = input("Input redirected URL: ")

    code = oauth.parse_response_code(url)
    oauth.set_token(code)

    client = Spotify(oauth)

    while True:
        track = client.get_the_users_currently_playing_track(market="from_token")

        if track is not None:
            print(f"[{dt.now()}] {track['item']['name']}")
        else:
            print(f"[{dt.now()}] no track playing")

        time.sleep(60)


if __name__ == "__main__":
    main()
