# Authored by: Desperauxq

import SimpleHTTPServer
import SocketServer

# PORT location, I choose 8000 as usual
PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Serving at port", PORT
httpd.serve_forever()
