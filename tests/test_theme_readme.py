from pathlib import Path
import importlib.util
import tempfile
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "theme_readme.py"
SPEC = importlib.util.spec_from_file_location("theme_readme", MODULE_PATH)
theme_readme = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(theme_readme)


class ThemeReadmeTests(unittest.TestCase):
    def test_restores_default_theme_from_halloween_readme(self):
        source_readme = Path(__file__).resolve().parents[1] / "profile" / "README.md"

        with tempfile.TemporaryDirectory() as tmpdir:
            readme_path = Path(tmpdir) / "README.md"
            readme_path.write_text(source_readme.read_text(encoding="utf-8"), encoding="utf-8")

            original_readme = theme_readme.README
            original_is_halloween = theme_readme.is_halloween
            theme_readme.README = readme_path
            theme_readme.is_halloween = lambda: False
            try:
                theme_readme.main()
            finally:
                theme_readme.README = original_readme
                theme_readme.is_halloween = original_is_halloween

            updated = readme_path.read_text(encoding="utf-8")
            self.assertIn(theme_readme.DEFAULT_HERO, updated)
            self.assertIn(theme_readme.DEFAULT_FOOTER, updated)
            self.assertNotIn("<!-- SEASONAL:START -->", updated)


if __name__ == "__main__":
    unittest.main()
