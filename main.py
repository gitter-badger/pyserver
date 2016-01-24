# Authored by: Desperauxq

import http.server
import socketserver

# PORT location, I choose 8000 as usual
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()
