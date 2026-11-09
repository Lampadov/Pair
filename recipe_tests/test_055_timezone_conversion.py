"""Execute the documented timezone conversion recipe as a regression test."""
from pathlib import Path
import re
import unittest


class Recipe055Test(unittest.TestCase):
    def test_timezone_conversion(self):
        document = Path(__file__).resolve().parents[1] / "docs/recipes/055-timezone-conversion.md"
        blocks = re.findall(r"```python\n(.*?)\n```", document.read_text(encoding="utf-8"), re.DOTALL)
        self.assertEqual(len(blocks), 1, "Expected exactly one Python recipe")
        self.assertTrue(blocks[0].strip(), "The recipe must contain executable code")
        exec(compile(blocks[0], str(document), "exec"), {"__name__": "__main__"})
