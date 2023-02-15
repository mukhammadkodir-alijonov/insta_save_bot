from os import link
import requests
import json
def instadownloader(link):
    
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
    
    querystring = {"url":link}

   
    headers = {
	"X-RapidAPI-Key": "1d3ecb0144msh4f7e65210867da5p1aa965jsnafe51198f4ea",
	"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    rest = json.loads(response.text)
    
    if 'error' in rest:
        return 'Bad'
    else:
        dict = {}
        if rest['Type'] == 'Post-Image':
            dict['type'] = 'image'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Post-Video':
              dict['type'] = 'video'
              dict['media'] = rest['media']
              return dict
        elif rest['Type'] == 'Carousel':
              dict['type'] = 'carousel'
              dict['media'] = rest['media']
              return dict
        else:
            return 'Bad'



