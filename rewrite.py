"""
The only reason why this file exists is cause it is easier for me to test stuff here.
Once the PR is finalized and all tests work, remove this file.
"""


import json
import re
from ast import literal_eval
from bs4 import BeautifulSoup, UnicodeDammit
from html import unescape


def bs(page_txt):
    html = BeautifulSoup(page_txt, "html.parser")
    lyrics_path = html.find("div", class_="lyrics")  # finding div on Genius containing the lyrics
    if lyrics_path:
        lyrics = UnicodeDammit(lyrics_path.get_text().strip()).unicode_markup
    else:
        # hotfix!
        lyrics_path = html.find_all("div", class_=re.compile("^Lyrics__Container"))
        lyrics_data = []
        for x in lyrics_path:
            lyrics_data.append(UnicodeDammit(re.sub("<.*?>", "", str(x).replace("<br/>", "\n"))).unicode_markup)

        lyrics = "\n".join(lyrics_data)
    return lyrics


json_regex = re.compile(r"window\.__PRELOADED_STATE__ = JSON\.parse\((.*)\);")
meta_regex = re.compile(r"<meta content=\"(.*)\" itemprop=\"page_data\"></meta>")
html_strip_regex = re.compile(r"<[\s\S]*?>")


def process_json_lyrics(body):
    lyrics = []
    for i in body:
        if type(i) == dict:
            if i['tag'] in ['p', 'i', 'a', 'b', 'u']:
                lyrics += process_json_lyrics(i['children'])
            elif i['tag'] in ['br', 'inread-ad']:
                lyrics.append("\n")
        elif type(i) == list:
            lyrics += process_json_lyrics(i)
        elif type(i) == str:
            lyrics.append(i)
        else:
            raise Exception(f"Unknown type occurred! Type = {type(i)}")
    return lyrics


def js(page_txt):
    json_data = json_regex.findall(page_txt)
    if len(json_data) == 0:
        meta_data = meta_regex.findall(page_txt)
        assert len(meta_data) == 1
        data = json.loads(unescape(meta_data[0]))
        lyrics_html = data['lyrics_data']['body']['html']
        lyrics = html_strip_regex.sub("", lyrics_html).strip()
    else:
        json_data = json_data[0]
        json_data = literal_eval(json_data)
        json_data = json_data.replace("\\$", "$")
        data = json.loads(json_data)
        lyrics = process_json_lyrics(data['songPage']['lyricsData']['body']['children'])
        lyrics = "".join(lyrics)
    return lyrics


with open('old.html', 'r') as f:
    old = f.read()

with open('new.html', 'r') as f:
    new = f.read()

# print(js(old))
# print(bs(old).strip() == bs(new).strip())
# print("-" * 20)
# print(bs(old))

# """
import time

t = time.time()
N = 100
for _ in range(N):
    js(old)
print((time.time() - t) / N)

t = time.time()
for _ in range(N):
    bs(old)
print((time.time() - t) / N)
# """
