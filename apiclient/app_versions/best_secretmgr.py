import urllib.request
import urllib.error
import os
import time
import sys
import logging

jotfile="/run/secrets/jot"
jwt=''
if os.path.isfile(jotfile):
    with open(jotfile) as jwtfile:
         for line in jwtfile:
             clean=line.strip()
             jwt="Bearer  "+ clean
else: 
    print("Error:file not present ", file=sys.stderr)
    sys.exit(1)
    
req = urllib.request.Request('http://host.docker.internal')
req.add_header("Authorization", jwt)
while True:
    time.sleep(5)
    try:
        with urllib.request.urlopen(req) as response:
                 the_page = response.read()
                 message = response.getheader('X-MESSAGE')
                 print("200  " + message, file=sys.stderr)
                 logging.warning(message)
    except urllib.error.URLError as e:
          print(str(e.code) + "  " + e.msg, file=sys.stderr) 
          logging.warning(e.msg)
