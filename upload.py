__author__ = 'vivitsu'

import dropbox


def upload(access_token, filename):
    client = dropbox.client.DropboxClient(access_token)
    path = '/' + filename
    f = open(filename, 'rb')
    response = client.put_file(path, f)
    print("uploaded:", response)
