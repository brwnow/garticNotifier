import urllib.request

class GarticRequester:
    GARTIC_BASE_URL = "https://www.gartic.com.br"

    HTTP_REQUEST_HEADER = {  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8' }

    GARTIC_FRIENDS_ENDPOINT = "/amigos"
    GARTIC_FRIENDS_PAG_ATT = "pag"

    def getProfileHtml(self, username):
        return self.doRequest(username)

    def getFriendsPage(self, username, pageNumber):
        return self.doRequest(username + self.GARTIC_FRIENDS_ENDPOINT, {self.GARTIC_FRIENDS_PAG_ATT: pageNumber})

    def doRequest(self, route, attMap = {}):
        requestUrl = self.GARTIC_BASE_URL + "/" + route

        if len(attMap) > 0:
            requestUrl = requestUrl + "/?"
            for item in attMap.items():
                requestUrl = requestUrl + item[0] + "=" + str(item[1])

        request = urllib.request.Request(requestUrl, headers=self.HTTP_REQUEST_HEADER)
        return urllib.request.urlopen(request).read()
