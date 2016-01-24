#!/usr/bin/python3

# Authored by: Desperauxq

import http.server
import socketserver

# PORT location, 8000 for IR
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()
