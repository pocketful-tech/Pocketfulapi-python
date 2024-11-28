""" 
----------Oauth2 Login Process-----------
After generating App Id and App Secret from the Pocketful API portal, if you are using a custom redirect URL, then you need to go through the below process of Oauth2 Login to generate access token. 
If you have used default redirect url, then you can directly generate access token from the Pocketful API portal.
In the below example we have used redirect url as localhost:8000/api-redirect.
"""

import requests
import webbrowser
import base64
import json
from flask import Flask, request

app = Flask(__name__)

# Configurable variables
APP_ID = ""
APP_SECRET = ""
REDIRECT_URI = "http://localhost:8080/api-redirect"
AUTH_URL = "https://trade.pocketful.in/oauth2/auth"
TOKEN_URL = "https://trade.pocketful.in/oauth2/token"


@app.route('/api-redirect', methods=['GET'])
def handle_redirect():
    """
    Handles the OAuth2 redirect, extracts the authorization code, 
    and exchanges it for an access token.
    """
    # Extract query parameters
    auth_code = request.args.get('code')
    state = request.args.get('state')
    scope = request.args.get('scope')

    if not auth_code:
        return "Authorization code missing!", 400

    # Exchange the authorization code for an access token
    payload = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': REDIRECT_URI,
    }

    credentials = f"{APP_ID}:{APP_SECRET}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        # 'Authorization': f'Basic {requests.auth._basic_auth_str(APP_ID, APP_SECRET)}',
        'Authorization': f'Basic {encoded_credentials}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(TOKEN_URL, headers=headers, data=payload)

    if response.status_code == 200:
        token_response = response.json()
        # Get the client id
        url = "https://trade.pocketful.in/api/v1/user/trading_info"
        headers = {
            'Authorization': f"Bearer {token_response.get('access_token')}",
            }
        response = requests.get(url, headers=headers)
        res = response.json()
        client_id = res['data']['client_id']
        access_token = token_response.get("access_token")
        with open("credentials.json", "w") as f:
            json.dump({"client_id": client_id, "access_token": access_token}, f)
        return f"Client ID: {client_id}, Access Token: {access_token}", 200
    else:
        return f"Failed to fetch access token: {response.text}", 400


def open_auth_url():
    """
    Constructs the OAuth2 authorization URL which will be opened in the default browser.
    """
    params = {
        "scope": "orders holdings",
        "state": "bdkjbcjhdbsvhj",  # Replace with your state value, any random unique value with minimum 8 characters
        "redirect-uri": REDIRECT_URI,
        "response_type": "code",
        "client_id": APP_ID
    }

    # Construct the authorization URL
    from urllib.parse import urlencode
    auth_url = f"{AUTH_URL}?{urlencode(params)}"

    # Open the URL in the default browser
    webbrowser.open(auth_url)


if __name__ == '__main__':
    # Step 1: Open the authorization URL
    open_auth_url()

    # Step 2: Start the Flask server to handle the redirect
    print("Starting Flask server to handle the redirect...")
    app.run(port=8080)
