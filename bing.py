# -*- coding: UTF-8 –*-

import httplib2
import os.path
import sys

h = httplib2.Http('cache')
url = 'http://www.bing.com/'
try:
    response, content = h.request(url, 'GET')
except:
    print('Bing homepage not opened.')
    sys.exit(1)


htmlContent = content.decode('utf-8')
imageUrl = htmlContent[htmlContent.find(';g_img'):]
imageUrl = imageUrl[imageUrl.find("'") + 1:]
imageUrl = imageUrl[:imageUrl.find("'")]
imageUrl = imageUrl.replace('1366x768', '1920x1080')

print(imageUrl)
if not imageUrl.endswith('jpg'):
    print('Image file not found.')
    sys.exit(2)

try:
    response, content = h.request(imageUrl, 'GET')
except:
    print('Image file not downloaded.')
    sys.exit(3)

try:
    imageFile = open(os.path.basename(imageUrl), 'wb')
    imageFile.write(content)
    imageFile.close()
except:
    print('File not saved.')
    sys.exit(4)

