import requests
import feedparser
import re
import json

headers = {
    'Content-Type': 'application/json',
    }

def getRSSFeed(alasVersion):
    alasUrl = "https://alas.aws.amazon.com/alas.rss"
    alas2Url = "https://alas.aws.amazon.com/AL2/alas.rss"
    alas2023Url = "https://alas.aws.amazon.com/AL2023/alas.rss"
    
    if alasVersion == "alas":
        return alasUrl
    elif alasVersion == "alas2":
        return alas2Url
    elif alasVersion == "alas2023":
        return alas2023Url
    else:
        raise Exception("Invalid ALAS version")

def parseRSSFeed(alasVersion):
    feedData = {
        "title": "",
        "link": "",
        "description": "",
        "entries": [],
    }
    
    cves = []

    try:
        response = requests.get(getRSSFeed(alasVersion), headers=headers)
        response.raise_for_status()
        feed = feedparser.parse(response.content)
        
        for entry in feed.entries:
            entryDetails = {}
            entryDetails["alasID"] = matchALAS(entry.title)
            entryDetails["title"] = entry.title
            entryDetails["description"] = matchCVE(entry.description)
            entryDetails["published"] = entry.published
            entryDetails["updated"] = entry.updated
            entryDetails["guid"] = entry.guid
            entryDetails["link"] = entry.link
            #entries["entry"].append(entryDetails)
            feedData["entries"].append(entryDetails)

        feedData["title"] = feed.feed.title
        feedData["link"] = feed.feed.link
        feedData["description"] = feed.feed.description
        #feedData["entries"] = entries
        return feedData
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def matchALAS(alasVersion):
    pattern = r'ALAS-\d{4}-\d*'
    match = re.findall(pattern, str(alasVersion))
    if match:
        return match
    else:
        return None

def matchCVE(cveID):
    pattern = r'CVE-\d{4}-\d*'
    match = re.findall(pattern, str(cveID))
    if match:
        return match
    else:
        return None

def main():
    alasVersion = "alas"
    alasData = parseRSSFeed(alasVersion)
    #print(alasData)
    print(json.dumps(alasData, indent=4, sort_keys=True))
    print(alasData)   

if __name__ == "__main__":
    main()