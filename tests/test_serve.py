from pathlib import Path
import tempfile
import unittest

from scripts import serve


class LocalServeRendering(unittest.TestCase):
    def test_known_nested_html_routes_resolve_inside_repo(self):
        for route in ("/", "/index.html", "/v7-preview/", "/v7-preview/index.html", "/v7-preview/shell-test.html"):
            path = serve.html_path_for_request(route)
            self.assertIsNotNone(path, route)
            self.assertTrue(path.is_file(), route)
            self.assertTrue(path.resolve().is_relative_to(serve.ROOT.resolve()), route)

    def test_non_html_and_traversal_do_not_enter_template_renderer(self):
        self.assertIsNone(serve.html_path_for_request("/v7-preview/app.js"))
        self.assertIsNone(serve.html_path_for_request("/../outside.html"))

    def test_render_html_strips_front_matter_and_replaces_revision(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.html"
            path.write_text("---\n---\n<link href='x.css?v={{ site.github.build_revision }}'>", encoding="utf-8")
            rendered = serve.render_html(path, "abc123")
        self.assertEqual(rendered.decode(), "<link href='x.css?v=abc123'>")
        self.assertNotIn("{{ site.github.build_revision }}", rendered.decode())


if __name__ == "__main__":
    unittest.main()
