#!/usr/bin/python3
import socket 
import re
import sys

url = sys.argv[1]

web_site = re.findall('http://(.+)/', url)[0]
requested_file = re.findall('http://.+/(.+)', url)[0]

http_port = 80
get_request = f'GET http://{web_site}/{requested_file} HTTP/1.0\r\n\r\n'.encode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((web_site, http_port)) 
except:
    print('Error occur')
    sys.exit()


s.send(get_request)

full_msg = ''
while True:
    msg = s.recv(8).decode("utf-8")
    if len(msg) <= 0: break
    full_msg += msg 


s.close()
print(full_msg)
