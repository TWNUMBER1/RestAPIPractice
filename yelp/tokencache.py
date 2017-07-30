import requests
import datetime as Datetime

class Authorization(object):

    __instance = None

    _token = None
    _tokenExpiresIn = None  # seconds
    _tokenDate = None       # Datetime
    _clientId = '4yjWaOYKr4bjL9ZJ2U7gQA'
    _clientSecret = 'YZJ6RbWH2IXMgp4F5fzVHyQKoLNpWI2pOEWYiYLuOrY1ziWcK0AgSL77ALaxwXSK'

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            cls.updateToken(cls._clientId, cls._clientSecret)
        return cls.__instance

    def getToken(self):
	currTime = Datetime.datetime.now()
	if (currTime - Authorization._tokenDate).total_seconds() >= Authorization._tokenExpiresIn: 
	    Authorization.updateToken(Authorization._clientId, Authorization._clientSecret)
        return Authorization._token

    @classmethod
    def updateToken(cls, id, secret):
	print("updating token... id=%s, secret=%s" %(id, secret))
        authUrl = 'https://api.yelp.com/oauth2/token'
        payload = {
            'grant_type': 'client_credentials',
	    'client_id': id,
	    'client_secret': secret
	}         
	headers = {
	    'content-type': 'application/x-www-form-urlencoded'
	}
        r = requests.post(authUrl, data=payload, headers=headers)
	try:
	    response = r.json()
            cls._token = { 'Authorization': response['token_type'] + ' ' +  response['access_token'] }
            cls._tokenExpiresIn = response['expires_in']
	    cls._tokenDate = Datetime.datetime.now()
	except KeyError as e:
	    print e
            return None
