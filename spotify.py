import requests
from urllib.parse import urlencode
import base64
import webbrowser

client_id = "91285b760df243868fa63954b68b769d"
client_secret = "351ac03829db4b2998758499462c45de"
# code = "AQBXJZdE-V4Q6Lxi6KDPz6yddjMevooe1cf3msf66LBenn3UoN81l4KwCh3zx8_4BgdVDgGMjGfMwDopMTNjUh_VaGUneeLnum1RwTiVJ36IIJzT7GHp5D1bWmGi6SsPLXM6W2yFtWUUmN6B76YogUA9bkGP9Kh349ilxwBylorbfyJE0gGxqAwq2rdQ-uIQDErh"

auth_headers = {
    "client_id": client_id,
    "response_type": "code",  # sends a request to retrieve an authorization code <temporary>
    "redirect_uri": "http://localhost:5000/search",
    "scope": "user-library-read"
}

webbrowser.open("https://accounts.spotify.com/authorize?" +
                urlencode(auth_headers))
