#!/usr/bin/env python3
import time
import random
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
PORT = 8080

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = parse.urlparse(self.path)

        if parsed_path.path == '/metrics':
            ts = int(time.time() * 1000)
            message = """# HELP sample_http_requests_total The total number of HTTP requests.
# TYPE sample_http_requests_total counter
sample_http_requests_total{{method="post",code="200"}} {} {}
sample_http_requests_total{{method="post",code="400"}}    {} {}
""".format(
    random.randint(100, 400), ts,
    random.randint(1, 100), ts)
        else:
            message = "I'm ok ~"

        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('', PORT), MyHandler)
    print(f'Starting server at {PORT}, use <Ctrl-C> to stop')
    server.serve_forever()
