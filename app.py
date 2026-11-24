import datetime
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (
            f"<h1>OS Lab - Cloud Deployment</h1>"
            f"<p>Served by host: {socket.gethostname()}</p>"
            f"<p>Time: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}</p>"
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
