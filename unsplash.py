import requests
import time
import json
from requests.structures import CaseInsensitiveDict

def unsplash_keywords():

    key_words = [
        'face', 'man', 'woman', 'lady', 'lass', 'lad', 'boy' 'girl', 
        'child', 'baby', 'hombre', 'senor', 'senorita', 'mujer', 
        'fraulein', 'frau', 'dama', 'grossvater', 'malchik', 'babe', 
        'master', 'bonita', 'chica', 'abuela', 'black man', 'white man', 
        'asian man', 'old man', 'old woman', 'happy girl outdoor', 'sad person', 
        'black baby', 'black girl', 'black woman', 'happy baby', 'queen', 
        'ugly girl', 'ugly boy', 'little boy', 'little girl', 'chinese lady', 'dirty boy',
        'asian woman'
        ]

    for keyword in key_words:
        url = f"https://api.unsplash.com/search/photos?query={keyword}&client_id=YOUR-API-KEY"

        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer {token}"

        resp = requests.get(url, headers=headers)
        our_json = json.loads(resp.text)
        time.sleep(1)

    return our_json
##################  The Code Below Is a slight modification to try and get 50 records every hour without having to rerun the program  ###################
# import requests
# import time
# import json
# from requests.structures import CaseInsensitiveDict

# def unsplash_keywords():

#     key_words = [
#         'face', 'man', 'woman', 'lady', 'lass', 'lad', 'boy' 'girl', 
#         'child', 'baby', 'hombre', 'senor', 'senorita', 'mujer', 
#         'fraulein', 'frau', 'dama', 'grossvater', 'malchik', 'babe', 
#         'master', 'bonita', 'chica', 'abuela', 'black man', 'white man', 
#         'asian man', 'old man', 'old woman', 'happy girl outdoor', 'sad person', 
#         'black baby', 'black girl', 'black woman', 'happy baby', 'queen', 
#         'ugly girl', 'ugly boy', 'little boy', 'little girl', 'chinese lady', 'dirty boy',
#         'asian woman'
#         ]
#     page = 1
#     while True:
#         url = f"https://api.unsplash.com/search/photos?query={key_words[32]}&client_id=SHlTuerJzZz-bp_wyS630dlLY8WGTMxx4ayelTUTNW0&per_page=50&page={page}"
#         headers = CaseInsensitiveDict()
#         headers["Accept"] = "application/json"
#         headers["Authorization"] = "Bearer {token}"
#         resp = requests.get(url, headers=headers)
#         our_json = json.loads(resp.text)
#         with open('photos.txt', 'a') as pt:
#             pt.write("%s\n" % our_json)
#         page+=1
#         time.sleep(3600)

# unsplash_keywords()

