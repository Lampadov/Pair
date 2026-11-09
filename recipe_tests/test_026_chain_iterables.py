"""Execute the documented chain iterables recipe as a regression test."""
from pathlib import Path
import re
import unittest


class Recipe026Test(unittest.TestCase):
    def test_chain_iterables(self):
        document = Path(__file__).resolve().parents[1] / "docs/recipes/026-chain-iterables.md"
        blocks = re.findall(r"```python\n(.*?)\n```", document.read_text(encoding="utf-8"), re.DOTALL)
        self.assertEqual(len(blocks), 1, "Expected exactly one Python recipe")
        self.assertTrue(blocks[0].strip(), "The recipe must contain executable code")
        exec(compile(blocks[0], str(document), "exec"), {"__name__": "__main__"})
