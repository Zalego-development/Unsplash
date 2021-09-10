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
