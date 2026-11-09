import unittest
from pair_progress import coauthors


class CoauthorTests(unittest.TestCase):
    def test_multiple_trailers(self):
        self.assertEqual(coauthors("Change\n\nCo-authored-by: Alice <a@example.org>\nCo-authored-by: Bob <b@example.org>\n"),
                         [("Alice", "a@example.org"), ("Bob", "b@example.org")])

    def test_plain_mention_is_not_a_trailer(self):
        self.assertEqual(coauthors("Discuss Co-authored-by: Alice <a@example.org>"), [])

    def test_invalid_address_is_not_counted(self):
        self.assertEqual(coauthors("Co-authored-by: Alice <not an address>"), [])


if __name__ == "__main__":
    unittest.main()
