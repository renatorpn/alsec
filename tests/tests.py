import unittest
import src
from src import getRSSFeed, parseRSSFeed, matchALAS

class TestAlas(unittest.TestCase):
    def test_getRSSFeed(self):
        self.assertEqual(getRSSFeed("alas"), "https://alas.aws.amazon.com/alas.rss")
        self.assertEqual(getRSSFeed("alas2"), "https://alas.aws.amazon.com/AL2/alas.rss")
        self.assertEqual(getRSSFeed("alas2023"), "https://alas.aws.amazon.com/AL2023/alas.rss")
        with self.assertRaises(Exception):
            getRSSFeed("alas3")

    def test_matchALAS(self):
        self.assertEqual(matchALAS("ALAS-2021-1234"), ["ALAS-2021-1234"])
        self.assertEqual(matchALAS("ALAS-2021-1234, ALAS-2021-1235"), ["ALAS-2021-1234", "ALAS-2021-1235"])
        self.assertEqual(matchALAS("ALAS-2021-1234, ALAS-2021-1235, ALAS-2021-1236"), ["ALAS-2021-1234", "ALAS-2021-1235", "ALAS-2021-1236"])
        self.assertEqual(matchALAS("ALAS-2021-1234, ALAS-2021-1235, ALAS-2021-1236, ALAS-2021-1237"), ["ALAS-2021-1234", "ALAS-2021-1235", "ALAS-2021-1236", "ALAS-2021-1237"])
        self.assertEqual(matchALAS("ALAS-2021-1234, ALAS-2021-1235, ALAS-2021-1236, ALAS-2021-1237, ALAS-2021-1238"), ["ALAS-2021-1234", "ALAS-2021-1235", "ALAS-2021-1236", "ALAS-2021-1237", "ALAS-2021-1238"])
        self.assertEqual(matchALAS("ALAS-2021-1234, ALAS-2021-1235, ALAS-2021-1236, ALAS-2021-1237, ALAS-2021-1238, ALAS-2021-1239"), ["ALAS-2021-1234", "ALAS-2021-1235", "ALAS-2021-1236", "ALAS-2021-1237", "ALAS-2021-1238", "ALAS-2021-1239"])
