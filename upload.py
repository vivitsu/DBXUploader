__author__ = 'vivitsu'

import dropbox

app_path = '/Apps/DBX Uploader/'

def upload(access_token, filename):
    client = dropbox.client.DropboxClient(access_token)
    path = app_path + filename
    f = open(filename, 'rb')
    response = client.put_file(path, f)
    print("uploaded:", response)
