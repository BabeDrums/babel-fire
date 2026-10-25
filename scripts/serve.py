"""Serve FIRE locally with an automatic Git build stamp: python3 scripts/serve.py.

GitHub Pages resolves the same Jekyll build-revision placeholders in production. This local
server mirrors that behavior for root FIRE, G7, and the G7 Shell Test so physical/local review
never depends on literal template placeholders or a stale manual cache key.
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
REVISION_TOKEN = "{{ site.github.build_revision }}"
FRONT_MATTER = "---\n---\n"


def current_commit() -> str:
    return subprocess.check_output(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True
    ).strip()


def html_path_for_request(request_path: str) -> Path | None:
    relative = request_path.lstrip("/")
    if not relative:
        relative = "index.html"
    elif request_path.endswith("/"):
        relative = f"{relative}index.html"
    path = (ROOT / relative).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError:
        return None
    if path.suffix.lower() != ".html" or not path.is_file():
        return None
    return path


def render_html(path: Path, commit: str) -> bytes:
    source = path.read_text(encoding="utf-8")
    if source.startswith(FRONT_MATTER):
        source = source[len(FRONT_MATTER):]
    return source.replace(REVISION_TOKEN, commit).encode()


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        request_path = urlsplit(self.path).path
        commit = None

        if request_path == "/build-info.json":
            commit = current_commit()
            data = json.dumps({"commit": commit}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        html_path = html_path_for_request(request_path)
        if html_path is None:
            return super().do_GET()

        commit = current_commit()
        data = render_html(html_path, commit)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
