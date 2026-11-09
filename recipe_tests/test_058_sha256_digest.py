"""Execute the documented sha256 digest recipe as a regression test."""
from pathlib import Path
import re
import unittest


class Recipe058Test(unittest.TestCase):
    def test_sha256_digest(self):
        document = Path(__file__).resolve().parents[1] / "docs/recipes/058-sha256-digest.md"
        blocks = re.findall(r"```python\n(.*?)\n```", document.read_text(encoding="utf-8"), re.DOTALL)
        self.assertEqual(len(blocks), 1, "Expected exactly one Python recipe")
        self.assertTrue(blocks[0].strip(), "The recipe must contain executable code")
        exec(compile(blocks[0], str(document), "exec"), {"__name__": "__main__"})
