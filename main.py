import urllib.request
from urllib.parse import urlparse
import shutil

url = 'http://static.googleusercontent.com/media/research.google.com/en/us/archive/mapreduce-osdi04.pdf'
o = urlparse(url)

# Will work only if there is no trailing '/'
path_elems = o.path.split('/')
filename = path_elems[-1]

with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)