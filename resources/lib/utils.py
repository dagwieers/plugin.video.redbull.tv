import re, urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse, json
import xml.etree.ElementTree as ET

def strip_url(url):
    nurl = re.search(r"\(\'(.*)\'\)", url)
    return nurl.group(1)

def build_url(base_url, query):
    return base_url + '?' + urllib.parse.urlencode(query)

def get_xml(url):
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.URLError as err:
        raise IOError(*err.reason)
    else:
        return ET.parse(response)

def get_json(url, token=None):
    try:
        request = urllib.request.Request(url)
        if token:
            request.add_header("Authorization", token)
        response = urllib.request.urlopen(request)
    except urllib.error.URLError as err:
        raise IOError(*err.reason)
    else:
        return json.loads(response.read())
