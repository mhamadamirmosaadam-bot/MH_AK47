import unittest

from my_app.main import greet


class GreetTests(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_named_greeting(self):
        self.assertEqual(greet("Copilot"), "Hello, Copilot!")


if __name__ == "__main__":
    unittest.main()
