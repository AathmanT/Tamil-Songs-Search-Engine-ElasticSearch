# Tamil-songs-search-engine-using-ElasticSearch

This repo contains 4216 songs data scraped from https://www.tamilpaa.com and stored at ```scraped_lyrics.txt``` file. Some of the metadata such as ```"இசையமைப்பாளர்", "நடிகர்கள்", "பாடியவர்கள்"``` are in English. ```web_scraping.py``` is used to scrap the data.

## Sample JSON data of scraped song
```
{
  "திரைப்படம்": "என்னை அறிந்தால்",
  "பாடல்_பெயர்": "அதாரு அதார",
  "இசையமைப்பாளர்": "Harris Jayaraj",
  "வருடம்": "2015",
  "நடிகர்கள்": "Ajith Kumar, Anushka Shetty, Trisha Krishnan",
  "பாடியவர்கள்": "Gaana Bala, Vijay Prakash",
  "பாடல்வரிகள்": "வா ராஜா வா வா அட இதான் ஒன் டாவா\nஇங்க எலாருக்கும் நோவா நெஞ்சு வலிக்குது ஸ்லோவா\nவா ராஜா வா வா அட இதான் ஒன் டாவா\nஇங்க எலாருக்கும் நோவா நெஞ்சு வலிக்குது ஸ்லோவா\nஆனது ஆச்சு நம்ம கைய மீறி போச்சு\nஅடி ஏன் வெட்டி பேச்சு ரொம்ப சோக்கா கீது மேட்ச்சு\nலுங்கியத்தான் தூக்கி கட்டு டஸ்டு படுது\nசேலையத்தான் ஏத்தி கட்டு ஹிப்பு தெரிது\nலுங்கியத்தான் தூக்கி கட்டு டஸ்டு படுது\nசேலையத்தான் ஏத்தி கட்டு ஹிப்பு தெரிது\nமங்கிப்போன மூஞ்சி எல்லாம் டாலடிக்குது\nசொங்கிப்போன நம்ம ஜனம் கூத்தடிக்குது\nஅதாரு அதாரு அதாரு அதாரு\nஉதாறு உதாறு காட்டாதே உதாறு\nஅதாரு அதாரு அதாரு அதாரு\nஉதாறு உதாறு காட்டாதே உதாறு\nஎல்லாமே இனி மேல் நல்லாதான் நடக்கும்\nபட்டாசும் சும்மாவே கொளுத்தாம வெடிக்கும்\nஅதாரு அதாரு அதாரு அதாரு\nஉதாறு உதாறு காட்டாதே உதாறு\nஎல்லாமே இனி மேல் நல்லாதான் நடக்கும்\nபட்டாசும் சும்மாவே கொளுத்தாம வெடிக்கும்\nவாச மல்லி வாசம் வீச வாசல் வரியா\nஉன் ஆசை எல்லாம்.. "}
```

Randomly selected 500 songs data are fully translated to Tamil and extra metadata such as ```"மதிப்பீடு", "வகை", "கிளிக்குகள்"``` are added to improve the quality of the search and stored as ```processed_lyrics.txt``` file. ```preprocess-finalize.py``` is used to produce these JSON data.

## Sample JSON data of a processed song
```
{
  "திரைப்படம்": "சகோ",
  "பாடல்_பெயர் ": "காதல் சைக்க",
  "இசையமைப்பாளர்": "எம். கிப்ரான்",
  "பாடல்வரிகள்": "ஓ முதல் சிரிப்பில் இதயத்தை எடுத்த\nஅடுத்த முறை உறக்கத்தை எடுத்த\nதெளிய வச்சு மயக்கத்தை கொடுத்த\nபெண்ணே உன் மேல்\nஎனக்கோ கிறுக்கோ கிறுக்கோ\n\nநீ சுத்த விட்ட லூப்பில் நானும் திரிஞ்சேன்\nநான் கெஞ்சி கெஞ்சி அஞ்சு கிலோ கொறைஞ்சேன்\nஉன் டின்டர் ப்ரொப்பைல் பாத்து கொஞ்சம் எரிஞ்சேன்\nஇதயத்தில் எனக்கிடம் இருக்கோ இருக்கோ\n\nநீ என்ன கேக்காத\nபொஸஸ்ஸிவ் ஆகாத\nஅழகிய ஆண்கள்\nஎன்ன கொஞ்சி பேச\n\nஅங்க கொஞ்சம் நெஞ்சம் ப்ரோக்கோ\nஇங்க பாரு காதல் சைக்கோ\nஇங்க பாரு காதல் சைக்கோ\n\n\nநான் அடக்கம் ஒழுக்கத்தின் டிக்சனரி\nபாத்ததுமே வணங்குற மாதிரி\nநான் அடக்கம் ஒழுக்கத்தின் டிக்சனரி\nபாத்ததுமே வணங்குற மாதிரி\nஉன் சந்தேகத்த நீ எரி\nநான் ஆல்மோஸ்ட் சீதைதான்\n\nஓ கண்ணே கண்ணே பார்\nநான்தான் உன் சௌக்கிதார்\nஉன் மனசுக்கு காவல்\nஉடம்புக்கு காதல்\n\nரெண்டும் தரும் தேகம் தேக்கோ\nஇங்க பாரு காதல் சைக்கோ\nஇங்க பாரு காதல் சைக்கோ",
  "பாடியவர்கள்": "அனிருத் ரவிச்சந்தர், த்வானி பானுஷாலி, தனிஷ்க் பாக்சி",
  "வருடம்": "2019",
  "நடிகர்கள் ": "பிரபாஸ், ஷ்ரத்தா கபூர்",
  "மதிப்பீடு": 5,
  "வகை": "மெல்லிசை பாடல், மெல்லிசைபாடல்",
  "கிளிக்குகள்": 267
}
```

Bulk API format of those 500 songs are stored as ```processed_lyrics_bulk_api.txt``` file

The following Query DSL are supported for all the diiferent types of user queries.

##  Query DSL for ElasticSearch search engine

 ```
 # deleting an index(database)
DELETE /songs_db


##########################################################################################
#########          This must be run before creating the index(database)       ############
#######      Make a folder named analysis in elasticserach config folder       ###########
####   Please copy tamil_stopwords.txt & tamil_stemming.txt to the analysis folder #######
##########################################################################################


# custom stop words and stemming new analyzer along with the standard analyzer
PUT /songs_db/
{
        "settings": {
            "analysis": {
                "analyzer": {
                    "my_analyzer": {
                        "tokenizer": "standard",
                        "filter": ["custom_stopper","custom_stems"]
                    }
                },
                "filter": {
                    "custom_stopper": {
                        "type": "stop",
                        "stopwords_path": "analysis/tamil_stopwords.txt"
                    },
                    "custom_stems": {
                        "type": "stemmer_override",
                        "rules_path": "analysis/tamil_stemming.txt"
                    }
                }
            }
        }
    }

# checking the custom analyzer(stopwords, stemming)
GET /songs_db/_analyze
{
  "text": ["மிகவும் இனிமையான ஒரு 10 பாடல்கள்"],
  "analyzer": "my_analyzer"
}

# Uploading data using bulk API
POST /_bulk
{ "index" : { "_index" : "songs_db", "_type" : "songs", "_id" :1 } }
{"திரைப்படம்": " சாஹோ ", "பாடலாசிரியர்": " விக்னேஸ் சிவன் ", "இசையமைப்பாளர்": "M. ஜிப்ரான் ", "பாடல்": "Bad Boy", "வருடம்": "2019", "பாடியவர்கள்": " பென்னி டயால் ,சுனிதா சாரதி ", "பாடல்வரிகள்": "Coming Soon", "மதிப்பீடு": "2", "வகை": "குத்து பாடல்"}
{ "index" : { "_index" : "songs_db", "_type" : "songs", "_id" :2 } }
{"திரைப்படம்": " சாஹோ ", "பாடலாசிரியர்": " விக்னேஸ் சிவன் ", "இசையமைப்பாளர்": "M. ஜிப்ரான் ", "பாடல்": "Bad Boy", "வருடம்": "2019", "பாடியவர்கள்": " பென்னி டயால் ,சுனிதா சாரதி ", "பாடல்வரிகள்": "Coming Soon", "மதிப்பீடு": "2", "வகை": "குத்து பாடல்"}

# Using custom indexing for search
# ஹரிஸ் ஜெயராஜ் songs spelling mistake
GET /songs_db/songs/_search
{
    "query": {
        "multi_match" : {
            "query" : "ஹஷ்ரி ஜெராயஜ்",
            "fuzziness": "AUTO",
	    "analyzer": "my_analyzer"
        }
    }
}

# Using standard indexing for search
# ஹரிஸ் ஜெயராஜ் songs spelling mistake
GET /songs_db/songs/_search
{
    "query": {
        "multi_match" : {
            "query" : "ஹஷ்ரி ஜெராயஜ்",
            "fuzziness": "AUTO",
	    "analyzer": "standard"
        }
    }
}

# top 10 songs from 1990 to 2020 using கிளிக்குகள்"
GET /songs_db/songs/_search
{
    "size" : 10,
     "sort" : [
        { "கிளிக்குகள்" : {"order" : "desc"}}
    ],
    "query": {
        "range" : {
            "வருடம்" : {
                "gte" : "2005",
                "lte" :  "2020"
            }
        }
    }
}

# top 10 songs from 1990 to 2020 using மதிப்பீடு"
GET /songs_db/songs/_search
{
    "size" : 10,
     "sort" : [
        { "மதிப்பீடு" : {"order" : "desc"}}
    ],
    "query": {
        "range" : {
            "வருடம்" : {
                "gte" : "2005",
                "lte" :  "2020"
            }
        }
    }
}

# top 10 songs from 2005 to 2020 filter output
GET /songs_db/songs/_search?filter_path=hits.hits._source.பாடல்_பெயர்,hits.hits._source.திரைப்படம்,hits.hits._source.வருடம்
{
    "size" : 10,
     "sort" : [
        { "மதிப்பீடு" : {"order" : "desc"}}
    ],
    "query": {
        "range" : {
            "வருடம்" : {
                "gte" : "2005",
                "lte" :  "2020"
            }
        }
    }
}

# top 10 songs from 2015 to 2020 filter output
GET /songs_db/songs/_search
{
    "_source":["திரைப்படம்", "பாடல்_பெயர்" ],
    "size" : 10,
     "sort" : [
        { "மதிப்பீடு" : {"order" : "desc"}}
    ],
    "query": {
        "range" : {
            "வருடம்" : {
                "gte" : "2015",
                "lte" :  "2020"
            }
        }
    }
}


#  top 10 songs from 2017
GET /songs_db/songs/_search
{
    "size":10,
    "sort" : [
        { "மதிப்பீடு" : {"order" : "desc"}}
    ],
    "query": {
        "multi_match": {
	          "query" : "2017",
            "fields":["வருடம்"],
            "fuzziness": "AUTO"
        }
    }
}

#  top 10 songs from 2017
GET /songs_db/songs/_search
{
    "size":10,
    "sort" : [
        { "மதிப்பீடு" : {"order" : "desc"}}
    ],
    "query": {
        "match": {
            "வருடம்": {
            "query": "2017",
            "fuzziness": "AUTO"
            }
        }
    }
}


# search by lyrics spelling mistake
GET /songs_db/_search
{
  "query": {
    "multi_match" : {
      "query":    "தூனவாம் தூவ தூவ ழைம துளிளிகல் உன்",
      "fuzziness": "AUTO"
    }
  }
}

# ஏ.ஆர்.ரஹ்மான் songs boosting பாடியவர்கள் by 3
GET /songs_db/_search
{
    "query": {
        "multi_match" : {
            "query" : "ஏ.ஆர்.ரஹ்மான்",
            "fields": ["இசையமைப்பாளர்", "பாடியவர்கள்^3"]
        }
    }
}

# இளையராஜா 2020 songs
GET /songs_db/_search
{
 "query": {
   "bool": {
         "must": [
             { "match": { "இசையமைப்பாளர்": "இளையராஜா" }},
             { "match": { "வருடம்": "2020" }}
         ]
       }
     }
   
}

# இளையராஜா latest songs using bool must
GET /songs_db/_search
{
  "query": {
    "bool": {
      "must": [{
          "match": {
            "இசையமைப்பாளர்": "இளையராஜா"
          }
        },
        {
          "range": {
            "வருடம்" : {
                "gte" : "2005"
            }
          }
        }
      ]
    }
  }
}

# ஏ.ஆர்.ரஹ்மான் இசையமைத்த ஆனால் ஏ.ஆர்.ரஹ்மான் பாடாத குத்துபாடல் or மெல்லிசைபாடல்
GET /songs_db/_search
{
  "query": {
    "bool": {
      "must": {
        "bool" : { 
          "should": [
            { "match": { "வகை": "குத்துபாடல்" }},
            { "match": { "வகை": "மெல்லிசைபாடல்" }} 
          ],
          "must": { "match": { "இசையமைப்பாளர்": "ஏ.ஆர்.ரஹ்மான்" }} 
        }
      },
      "must_not": { "match": {"பாடியவர்கள்": "ஏ.ஆர்.ரஹ்மான்" }}
    }
  }
}

# இளையராஜா latest songs using bool filter
GET /songs_db/_search
{
  "query": {
    "bool": {
      "must": [{
          "match": {
            "இசையமைப்பாளர்": "இளையராஜா"
          }
        }
      ],
      "filter": [ 
        {
          "range": {
            "வருடம்" : {
                "gte" : "2005"
            }
          }
        }
      ]
    }
  }
}

# ஏ.ஆர்.ரஹ்மான் இசையமைத்த ஆனால் ஏ.ஆர்.ரஹ்மான் பாடாத 2009 இற்கு பிந்திய குத்துபாடல் or மெல்லிசைபாடல்
GET /songs_db/_search
{
  "query": {
    "bool": {
      "must": {
        "bool" : { 
          "should": [
            { "match": { "வகை": "குத்துபாடல்" }},
            { "match": { "வகை": "மெல்லிசைபாடல்" }} 
          ],
          "filter": [ 
        {
          "range": {
            "வருடம்" : {
                "gte" : "2009"
            }
          }
        }
      ],
          "must": { "match": { "இசையமைப்பாளர்": "ஏ.ஆர்.ரஹ்மான்" }} 
        }
      },
      "must_not": { "match": {"பாடியவர்கள்": "ஏ.ஆர்.ரஹ்மான்" }}
    }
  }
}

# ஜி.வி.பிரகாஷ்குமார் இசையமைத்த 2008 இற்கு பிந்திய "மெல்லிசைபாடல்" output score is not calculated for filter conditions.
GET /songs_db/_search
{
    "query": {
        "bool": {
            "must" : {
                "multi_match": {
                    "query": "மெல்லிசைபாடல்",
                    "fields": ["வகை"]
                }
            },
            "filter": {
                "bool": {
                    "must": {
                        "range" : { "வருடம்": { "gte": 2008 } }
                    },
                    "should": {
                        "term": { "இசையமைப்பாளர்": "ஜி.வி.பிரகாஷ்குமார்" }
                    }
                }
            }
        }
    },
    "_source" : ["பாடல்_பெயர்","வருடம்","திரைப்படம்", "இசையமைப்பாளர்"]
}


# best குத்து பாடல்கள் 
GET /songs_db/_search
{
    "sort" : [
        { "மதிப்பீடு" : {"order" : "desc"}}
    ],
  "query": {
    "multi_match" : {
      "query":    "குத்து பாடல்",
      "fields":["வகை"],
      "fuzziness": "AUTO"
    }
  }
}

#இசையமைப்பாளர் name ending in ன்
GET /songs_db/_search
{
    "query": {
        "wildcard" : {
            "இசையமைப்பாளர்" : "*ன்"
        }
    },
    "_source": ["இசையமைப்பாளர்"],
    "highlight": {
        "fields" : {
            "இசையமைப்பாளர்" : {}
        }
    }
}

# top 10 குத்து பாடல்கள் 
GET /songs_db/_search
{
  "size":10,
    "sort" : [
        { "மதிப்பீடு" : {"order" : "desc"}}
    ],
  "query": {
    "multi_match" : {
      "query":    "குத்து பாடல்",
      "fields":["வகை"],
      "fuzziness": "AUTO"
    }
  }
}

#LATEST songs, new songs
GET /songs_db/_search
{
    "query": {
        "range": {
            "வருடம்" : {
                "gte" : "2017"
            }
        }
    }
}

# search songs by movie
GET /songs_db/_search
{
    "query": {
        "multi_match": {
            "fields":["திரைப்படம்"],
            "query" : "சமர்",
            "fuzziness": "AUTO"
        }
    }
}

#term query for exact match
GET /songs_db/_search
{
  "query": {
    "term": {
      "திரைப்படம்":"சமர்"
    }
  }
}

# for multiple indexes(databases) search
GET /_all/_search
{
  "query": {
    "term": {
      "திரைப்படம்":"சமர்"
    }
  }
}
```
