"""Serve FIRE locally with an automatic Git build stamp: python3 scripts/serve.py.

GitHub Pages renders build-info.json through its existing Jekyll build instead.
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path not in ("/build-info.json", "/", "/index.html"):
            return super().do_GET()
        commit = subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True
        ).strip()
        if path == "/build-info.json":
            data = json.dumps({"commit": commit}).encode()
            content_type = "application/json"
        else:
            source = (ROOT / "index.html").read_text()
            if source.startswith("---\n---\n"):
                source = source[8:]
            data = source.replace("{{ site.github.build_revision }}", commit).encode()
            content_type = "text/html; charset=utf-8"
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
