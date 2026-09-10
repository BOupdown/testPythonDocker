"""Minimal HTTP service used to demonstrate containerization with Docker."""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        routes = {
            "/": {"service": "python-docker-demo", "status": "ok"},
            "/health": {"status": "healthy"},
        }
        payload = routes.get(self.path)

        if payload is None:
            self.send_response(404)
            payload = {"error": "not found"}
        else:
            self.send_response(200)

        body = json.dumps(payload).encode("utf-8")
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


def main():
    port = int(os.environ.get("PORT", "8000"))
    server = HTTPServer(("0.0.0.0", port), RequestHandler)
    print(f"Python Docker demo listening on port {port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
