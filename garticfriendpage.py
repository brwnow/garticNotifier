from bs4 import BeautifulSoup
import re
import log

class GarticFriendPage:
    pageIndex = "0"
    maxPageIndex = "0"
    friendsList = []

    def __init__(self, rawPageData):
        # For some reason python uses the same list object for all GarticFriendPage instances
        # So it's necessary setting this att to an empty list every time GarticFriendPage is
        #instantiated
        self.friendsList = []

        soup = BeautifulSoup(rawPageData, 'lxml')

        log.log('Parsing gartic friends page')

        # Getting current page
        self.pageIndex = int(soup.find("a", class_="linkPaginacaoMarcado").contents[0])

        # Getting the total count of pages. First get the list of page buttons
        pageButtons = soup.find_all("a", class_="linkPaginacao")
        if(len(pageButtons) == 0):
            # There is only a single one page of friends
            self.maxPageIndex = 1
        else:
            # Lets get the last navigation button which points tot he last page
            buttonHref = self.maxPageIndex = pageButtons[-1].attrs["href"]

            # Extracting the number at the end of the href wich is the index of the last page
            self.maxPageIndex = int(re.search(r"\d+$", buttonHref).group())

        log.log('pageIndex: ' + str(self.pageIndex) + ' --- maxPageIndex: ' + str(self.maxPageIndex))

        for player in soup.find_all("div", class_="titulo"):
            self.friendsList.append(player.find("a").contents[0].replace("\n", "").lower().strip())

        log.log('friendsList: ' + str(self.friendsList))