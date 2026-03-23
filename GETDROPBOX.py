"""
One-time script to obtain a Dropbox refresh token.

Usage:
    python GETDROPBOX.py

You will be prompted for your App Key and App Secret (from the Dropbox
developer console), then directed to authorize the app in your browser.
Paste the authorization code back here and the refresh token will be printed.

Copy the refresh token into the Dropbox Settings page in the admin panel.
"""

from dropbox import DropboxOAuth2FlowNoRedirect

app_key = input("App Key: ").strip()
app_secret = input("App Secret: ").strip()

auth_flow = DropboxOAuth2FlowNoRedirect(app_key, app_secret, token_access_type="offline")

print("\nVisit this URL to authorize the app:")
print(auth_flow.start())

code = input("\nPaste the authorization code here: ").strip()
result = auth_flow.finish(code)

print("\nRefresh token:")
print(result.refresh_token)
print("\nCopy this token into Admin > Edit Dropbox Settings > Refresh Token.")
