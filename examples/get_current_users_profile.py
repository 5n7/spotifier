"""Example app to print your display name on Spotify."""

import os
import webbrowser

from spotifier import Spotify
from spotifier.oauth import SpotifyAuthorizationCode


def main():
    oauth = SpotifyAuthorizationCode(
        client_id=os.environ["SPOTIFY_CLIENT_ID"],
        client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
        redirect_uri=os.environ["SPOTIFY_REDIRECT_URI"],
    )

    webbrowser.open(oauth.get_authorize_url())
    url = input("Input redirected URL: ")

    code = oauth.parse_response_code(url)
    oauth.set_token(code)

    client = Spotify(oauth)

    print(client.get_current_users_profile()["display_name"])


if __name__ == "__main__":
    main()
