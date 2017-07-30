import requests
import tokencache

tokenCache = tokencache.Authorization()

token = tokenCache.getToken()

payload = { 'term': 'Restaurant Week',
            'location': 'ny',
            'sort_by': 'rating' }

searchUrl = 'https://api.yelp.com/v3/businesses/search'
r = requests.get(searchUrl, headers=token, params=payload)

print r.json()

