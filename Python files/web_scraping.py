import requests
import numpy as np
import pandas as pd
import json
from bs4 import BeautifulSoup
import codecs
import unicodedata

url = 'https://www.tamilpaa.com/tamil-movies-list'
movies = []
r = requests.get(url)
content = r.content
soup = BeautifulSoup(content)
detail_content = soup.find('table', attrs = {'class': 'standard mb-50px'})

tablecontent = detail_content.find_all('tr')
print("num_movies:",len(tablecontent))

for tr in tablecontent[1:]:
    song = {}
    a_tags = tr.find_all('a')
    td_tags = tr.find_all('td')
    
    song["movie_url"] = a_tags[0].get('href')
    song["வருடம்"] = td_tags[1].get_text()
    song["இசையமைப்பாளர்"] = td_tags[2].get_text()
    song["நடிகர்கள்"] = td_tags[3].get_text()
    movies.append(song)

print(len(movies))
print(movies[0])

songs_data = []
def crawl_movie_url(movie):
  # print(movie)
  r = requests.get(movie["movie_url"])
  content = r.content
  soup = BeautifulSoup(content)

  detail_content = soup.find('table', attrs = {'class': 'standard'})

  td_tags = detail_content.find_all('td')
  # print(tablecontent)
  movie["திரைப்படம்"]= td_tags[2].get_text()

  song_div = soup.find('div', attrs = {'class': 'tab-content clearfix', 'id': 'tab_1'})
  song_li_tags =song_div.find_all('li')
  
  for song_li in song_li_tags:
    song ={}
    song["திரைப்படம்"] = movie["திரைப்படம்"]
    s = song_li.find('a').get_text().split('(')
    song["பாடல்_பெயர்"]= s[1][:-3].strip('\n')
    song["இசையமைப்பாளர்"] = movie["இசையமைப்பாளர்"]
    song["வருடம்"] = movie["வருடம்"]
    song["நடிகர்கள்"] = movie["நடிகர்கள்"]
    song["song_url"]= song_li.find('a').get('href')
    songs_data.append(song)
    
i=0
for movie in movies:
  if(i%500==0):
    print(i)
  crawl_movie_url(movie)
  i+=1

print(len(songs_data))
print(songs_data[0])

final_data = []
def crawl_song_url(song):
  r = requests.get(song["song_url"])
  content = r.content
  soup = BeautifulSoup(content)
  detail_content = soup.find('table', attrs = {'class': 'standard mb-10px'})
  tablecontent =detail_content.find_all('td')
  # print(tablecontent)
  song["பாடியவர்கள்"]= tablecontent[4].get_text()

  # print(song)
  song_content = soup.find('div', attrs = {'class': 'info-box white-bg'})

  song["பாடல்வரிகள்"]= (song_content.get_text()).strip()
  del song["song_url"]
  final_data.append(song)
  # print(song)
    
i=0
for song in songs_data:
  if(i%500==0):
    print(i)
  try:
    crawl_song_url(song)
  except Exception as e:
    print("Error in")
    print(song)
    print(e)
  i+=1

print(len(final_data))
print(final_data[0])



f = codecs.open('scraped_lyrics.txt', 'w', encoding='utf-8')
i=1
for line in final_data:
  # if(i%500==0):
  #   print(i)
  try:
      song_json = str(line).replace("\'", "\"")
      # song_json["பாடல்வரிகள்"] = unicodedata.normalize("NFKD",song_json["பாடல்வரிகள்"])

      # json.dump(song_json, f, ensure_ascii=False)
      f.write(song_json)
      f.write('\n')
  except Exception as e:
      print(i)
      print("Error in")
      print(line)
      print(e)
  i += 1