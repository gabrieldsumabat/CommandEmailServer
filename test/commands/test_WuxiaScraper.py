import unittest

from bs4 import BeautifulSoup
from requests import get

from commands import WuxiaScraper


class TestWuxia(unittest.TestCase):
    def setUp(self):
        url = "https://www.wuxiaworld.com/novel/a-will-eternal/awe-chapter-1"
        self.soup = BeautifulSoup(get(url).text, "html.parser")

    def test_wuxia_title(self):
        fetched_title = WuxiaScraper.get_title(self.soup)
        self.assertEqual(fetched_title.strip(), "Chapter 1: I'm Bai Xiaochun",
                         "Incorrect Chapter Title!")

    def test_wuxia_body(self):
        fetched_chapter = WuxiaScraper.get_body(self.soup)
        self.assertTrue(fetched_chapter.__contains__(
            "Perhaps whatever it was that had been rustling around in the shrubbery"), "Missing chapter text!")


if __name__ == "__main__":
    unittest.main()
