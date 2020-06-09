# Authetitcates user
from pydrive.auth import GoogleAuth
import os


g_login = GoogleAuth()
# Try to load saved client credentials
g_login.LoadCredentialsFile("myCreds.txt")
if g_login.credentials is None:
    # Authenticate if they're not there
    g_login.LocalWebserverAuth()
elif g_login.access_token_expired:
    # Refresh them if expired
    g_login.Refresh()
else:
    # Initialize the saved creds
    g_login.Authorize()
# Save the current credentials to a file
g_login.SaveCredentialsFile("myCreds.txt")


# Source: https://stackoverflow.com/questions/24419188/automating-pydrive-verification-process
