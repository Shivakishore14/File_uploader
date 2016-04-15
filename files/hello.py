#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()

# Generator to buffer file chunks
def fbuffer(f, chunk_size=10000):
   while True:
      chunk = f.read(chunk_size)
      if not chunk: break
      yield chunk

fileitem = form['file']
videos=['avi','mp4','flv','mkv','wmv','3gp','mpg']
music=['mp4','midi']
documents=['doc','docx','pdf','ppt','pptx','doc','docx','odf','txt','rtf','xml','html','odt']
images=['jpg','gif','jpeg','png','bmp']
applications=["exe","rpm","deb","dmg","jar","jad","bin","apk","run","msi","pkg"]
# Test if the file was uploaded
if fileitem.filename:
   fn = os.path.basename(fileitem.filename)
   b=fn.find('.')
   c=(fn[b+1:]).lower()
   if c in videos:
	   filepath='videos/'
   elif c in music:
	   filepath='music/'
   elif c in documents:
	   filepath='documents/'
   elif c in images:
	   filepath='images/'
   elif c in applications:
	   filepath='applications/'
   else:
	   filepath='others/'
   if not os.path.exists(filepath):
	os.makedirs(filepath)
	
   f = open(filepath + fn, 'wb', 10000)

   for chunk in fbuffer(fileitem.file):
      f.write(chunk)
   f.close()
