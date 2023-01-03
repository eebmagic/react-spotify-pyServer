# server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:3000')
        self.end_headers()
        
        query_string = urlparse(self.path).query
        query_params = parse_qs(query_string)
        message = query_params.get('message', [''])[0]
        email = query_params.get('email', [''])[0]
        username = query_params.get('username', [''])[0]
        # print(f'query_string: {query_string}')
        # print(f'query_params: {query_params}')
        print(json.dumps(query_params, indent=2))
        print(f' message: {message}')
        print(f'   email: {email}')
        print(f'username: {username}')
        result = message[::-1]
        self.wfile.write(f'Reversed: {result}'.encode())

httpd = HTTPServer(('localhost', 8000), RequestHandler)
print(f'Server started...')
httpd.serve_forever()
