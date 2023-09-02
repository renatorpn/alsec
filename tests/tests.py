import unittest
import ..src.alas

class TestAlas(unittest.TestCase):
    def test_getALASFeed(self):
        self.assertEqual(alas.getALASFeed(), "https://alas.aws.amazon.com/alas.rss")

    def test_parseRSSFeed(self):
        self.assertEqual(alas.parseRSSFeed("alas"), "https://alas.aws.amazon.com/alas.rss")
        self.assertEqual(alas.parseRSSFeed("alas2"), "https://alas.aws.amazon.com/alas2.rss")
        self.assertEqual(alas.parseRSSFeed("alas2023"), "https://alas.aws.amazon.com/alas2023.rss")

    def test_getRSSFeed(self):
        self.assertEqual(alas.getRSSFeed("alas"), "https://alas.aws.amazon.com/alas.rss")
        self.assertEqual(alas.getRSSFeed("alas2"), "https://alas.aws.amazon.com/alas2.rss")
        self.assertEqual(alas.getRSSFeed("alas2023"), "https://alas.aws.amazon.com/alas2023.rss")

    def test_matchALAS(self):
        self.assertEqual(alas.matchALAS("ALAS-2021-1234: "), "ALAS-2021-1234")
    
    def test_matchCVE(self):
        self.assertEqual(alas.matchCVE("CVE-2021-1234: "), "CVE-2021-1234")
        
    def test_matchSeverity(self):
        self.assertEqual(alas.matchSeverity("critical"), "critical")
        self.assertEqual(alas.matchSeverity("important"), "important")
        self.assertEqual(alas.matchSeverity("medium"), "medium")
        self.assertEqual(alas.matchSeverity("low"), "low")
        
    def test_matchPackage(self):
        self.assertEqual(alas.matchPackage("ALAS-2021-1234 (CVE-2021-1234): package"), "package")