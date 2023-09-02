import requests
import feedparser
import re
import json
import alas as config

headers = {
    'Content-Type': 'application/json',
    }
class Alas:
    def __init__(self, alasVersion, alasData):
        self._alasVersion = None
        self._alasData = None
    
    @property
    def alasVersion(self):
        return self._alasVersion
    
    @alasVersion.setter
    def alasVersion(self, alasVersion):
        self._alasVersion = alasVersion
    
    @property
    def alasData(self):
        return self._alasData
    
    @alasData.setter
    def alasData(self, alasData):
        self._alasData = alasData
    
    @staticmethod
    def _getRSSFeedAlasv1():
        return config.alasURL
    
    @staticmethod
    def _getRSSFeedAlasv2():
        return config.alas2URL
    
    @staticmethod    
    def _getRSSFeedAlasv2023():
        return config.alas2023URL
    
    def _parseRSSFeed(alasVersion):
        feedData = {
            "title": "",
            "link": "",
            "description": "",
            "entries": [],
        }
        
        try:
            response = requests.get(getRSSFeed(alasVersion), headers=headers)
            response.raise_for_status()
            feed = feedparser.parse(response.content)
            
            for entry in feed.entries:
                entryDetails = {}
                entryDetails["alasID"] = matchALAS(str(entry.title))
                entryDetails["title"] = str(entry.title)
                entryDetails["description"] = matchCVE(str(entry.description))
                entryDetails["severity"] = matchSeverity(str(entry.title))
                entryDetails["package"] = matchPackage(str(entry.title))
                entryDetails["published"] = str(entry.published)
                entryDetails["updated"] = str(entry.updated)
                entryDetails["guid"] = str(entry.guid)
                entryDetails["link"] = str(entry.link)
                feedData["entries"].append(entryDetails)

            feedData["title"] = str(feed.feed.title)
            feedData["link"] = str(feed.feed.link)
            feedData["description"] = str(feed.feed.description)
            return feedData
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    def _matchALAS(alasVersion):
        pattern = r'ALAS-\d{4}-\d*'
        match = re.findall(pattern, str(alasVersion))
        if match:
            return match
        else:
            return None

    def _matchCVE(cveID):
        pattern = r'CVE-\d{4}-\d*'
        match = re.findall(pattern, str(cveID))
        if match:
            return match
        else:
            return None

    def _matchSeverity(severity):
        pattern = r'critical|important|medium|low'
        match = re.findall(pattern, str(severity))
        if match:
            return match
        else:
            return None

    def _matchPackage(package):
        pattern = r'ALAS-\d{4}-\d{4} \(.*\): (.*.*)'
        match = re.findall(pattern, str(package))
        if match:
            return match
        else:
            return None

def main():
    alasVersion = "alas"
    alasObj = Alas(alasVersion, None)
    alasObj.alasVersion = alasVersion

    if alasObj.alasVersion == "alas":
        url = alasObj._getRSSFeedAlasv1()
    elif alasObj.alasVersion == "alas2":
        url = alasObj._getRSSFeedAlasv2()
    elif alasObj.alasVersion == "alas2023":
        url = alasObj._getRSSFeedAlasv2023()
    
    alasObj.alasData = alasObj._parseRSSFeed(alasVersion)
    alasData = alasObj.alasData
    print(json.dumps(alasData, indent=4, sort_keys=True))
    
if __name__ == "__main__":
    main()