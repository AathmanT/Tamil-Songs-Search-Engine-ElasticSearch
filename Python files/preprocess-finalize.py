import json
import codecs
import random


song_category = ["குத்து பாடல், குத்துபாடல் ","மெல்லிசை பாடல், மெல்லிசைபாடல்","கர்நாடக சங்கீதம், கர்நாடகசங்கீதம்","மேலைத்தேய சங்கீதம், மேலைத்தேயசங்கீதம்"]
f = codecs.open('processed_lyrics_bulk_api.txt', 'w', encoding='utf-8')

json_file = open("translated_lyrics.txt", encoding='utf-8', errors='ignore')

i=1
for line in json_file:
    try:
        print(i)
        song_json = json.loads(line)
        song_json["மதிப்பீடு"] = random.randint(1, 5)
        song_json["வகை"] = song_category[random.randint(0, 3)]
        song_json["கிளிக்குகள்"] = random.randint(1, 500)

        f.write('{ "index" : { "_index" : "songs_db", "_type" : "songs", "_id" :' + str(i) + ' } }\n')
        json.dump(song_json, f, ensure_ascii=False)
        f.write('\n')
        i += 1
        print(song_json)
        print()

    except Exception as e:
        print("Something else went wrong")





# for attribute, value in song_json.items():
#     # print(attribute, value)
#     song_json[attribute] = unicodedata.normalize("NFKD", str(value))

