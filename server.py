import http.server
import socketserver

PORT = 5000

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        '': 'application/octet-stream',
        '.mp3': 'audio/mpeg',
        '.html': 'text/html',
        '.m3u8': 'application/vnd.apple.mpegurl',
    }

httpd = socketserver.TCPServer(("localhost", PORT), HttpRequestHandler)

try:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
except KeyboardInterrupt:
    pass