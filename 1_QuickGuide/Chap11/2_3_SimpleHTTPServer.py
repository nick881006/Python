# Simple HTTPsERVER

import SocketServer
import SimpleHTTPServer

HOST = ''
PORT = 8000

# Create the server, SimpleHTTPRequestHander is pre-defined handler in SimpleHTTPServer package
server = SocketServer.TCPServer((HOST, PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)
# Start the server
server.serve_forever()