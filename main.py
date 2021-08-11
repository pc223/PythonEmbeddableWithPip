print("hello world")
import sys
print(sys.path)
import platform
print(platform.platform())

import requests


r = requests.get('https://google.com')
print(r.title)

import urllib.request

local_filename, headers = urllib.request.urlretrieve("https://www.python.org/ftp/python/3.8.9/python-3.8.9-embed-amd64.zip", "./")

print(local_filename, headers, sep='   |   ')


