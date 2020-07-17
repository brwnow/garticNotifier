import urllib.request

class GarticRequester:
    GARTIC_BASE_URL = "https://www.gartic.com.br"

    HTTP_REQUEST_HEADER = { 'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
                            'method': 'GET',
                            'scheme': 'https',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'none',
                            'upgrade-insecure-requests': '1',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7' }

    GARTIC_FRIENDS_ENDPOINT = "/amigos"
    GARTIC_FRIENDS_PAG_ATT = "pag"

    def __init__(self):
        pass

    def getProfileHtml(self, username):
        return self.__doRequest(username)

    def getFriendsPageHtml(self, username, pageNumber):
        return self.__doRequest(username + self.GARTIC_FRIENDS_ENDPOINT, {self.GARTIC_FRIENDS_PAG_ATT: pageNumber})

    def __doRequest(self, route, attMap = {}):
        requestUrl = self.GARTIC_BASE_URL + "/" + route

        if len(attMap) > 0:
            requestUrl = requestUrl + "/?"
            for item in attMap.items():
                requestUrl = requestUrl + item[0] + "=" + str(item[1])

        request = urllib.request.Request(requestUrl, headers=self.HTTP_REQUEST_HEADER)
        return urllib.request.urlopen(request).read()
