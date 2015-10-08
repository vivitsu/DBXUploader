import dropbox
import os
import sys


class DBX(object):

    TOKEN_FILE = "token.config"
    OAUTH_FILE = "oauth.config"
    access_token = None

    def __init__(self):
        self.__authenticate()

    def __authenticate(self):
        if os.path.exists("token.config"):
            self.access_token = DBX.__authenticate_using_token()
        else:
            self.access_token = DBX.__authenticate_using_oauth()

    # Parsing the config file can be done in a better way
    @staticmethod
    def __authenticate_using_oauth():
        with open(DBX.OAUTH_FILE, "r") as conf_file:
            app_key = conf_file.readline().strip()
            app_secret = conf_file.readline().strip()

        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

        # Have the user sign in and authorize this token
        authorize_url = flow.start()
        print "1. Go to: %s" % authorize_url
        print "2. Click \"Allow\" (you might have to log in first)"
        print "3. Copy the authorization code."
        code = input("Enter the authorization code here: ").strip()

        # This will fail if the user enters an invalid authorization code
        access_token, user_id = flow.finish(code)

        with open(DBX.TOKEN_FILE, "w") as token_file:
            token_file.write(access_token)

        return access_token

    @staticmethod
    def __authenticate_using_token():
        with open("token.config", 'r') as token_file:
            access_token = token_file.readline().strip()

        return access_token

    @staticmethod
    def __remove_cached_token():
        if os.path.exists(DBX.TOKEN_FILE):
            os.remove(DBX.TOKEN_FILE)
        else:
            print "Token file not found."

    def __retry_if_access_revoked(self, filename):
        print "Access to the app has been revoked. Retrying..."
        self.__authenticate()
        self.upload(filename)

    def __upload(self, filename):
        try:
            client = dropbox.client.DropboxClient(self.access_token)
        except ValueError as verr:
            self.__remove_cached_token()
            print verr
            print "Please try again."
            sys.exit(1)

        path = "/" + filename
        f = open(filename, "rb")
        try:
            response = client.put_file(path, f)
            print response
        except dropbox.rest.ErrorResponse as err:
            raise err

    def upload(self, filename):
        try:
            self.__upload(filename)
        except dropbox.rest.ErrorResponse as e:
            if e.status == 401:
                self.__remove_cached_token()
                self.__retry_if_access_revoked(filename)
            else:
                print e.reason

