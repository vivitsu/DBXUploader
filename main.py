import urllib.request
import shutil
import argparse
import urllib.parse
import os

from dbx import DBX

parser = argparse.ArgumentParser()
parser.add_argument("url", help="The URL of the file you want to upload")
args = parser.parse_args()
url = args.url
o = urllib.parse.urlparse(url)

'''
Will work in very select cases, for e.g.:
http://static.googleusercontent.com/media/research.google.com/en/us/archive/mapreduce-osdi04.pdf
'''
path_elems = o.path.split('/')
filename = path_elems[-1]

dbx = DBX()

# TODO: Check if file exists, and don't download if it does

with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

dbx.upload(filename)

if os.path.exists(filename):
    os.remove(filename)
else:
    print('File {f} not found.'.format(f=filename))