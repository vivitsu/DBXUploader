import dropbox


# Parsing the config file can be done in a better way
def using_oauth():
    with open('oauth.config', 'r') as conf_file:
        app_key = conf_file.readline().strip()
        app_secret = conf_file.readline().strip()

    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

    # Have the user sign in and authorize this token
    authorize_url = flow.start()
    print('1. Go to: ' + authorize_url)
    print('2. Click "Allow" (you might have to log in first)')
    print('3. Copy the authorization code.')
    code = input("Enter the authorization code here: ").strip()

    # This will fail if the user enters an invalid authorization code
    access_token, user_id = flow.finish(code)

    return access_token


def __using_token():
    with open('token.config', 'r') as token_file:
        token = token_file.readline().strip()

    return token