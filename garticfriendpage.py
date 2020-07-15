from bs4 import BeautifulSoup
import re

class GarticFriendPage:
    pageIndex = "0"
    maxPageIndex = "0"
    friendsList = []

    def __init__(self, rawPageData):
        soup = BeautifulSoup(rawPageData, 'lxml')

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

        for player in soup.find_all("div", class_="titulo"):
            self.friendsList.append(player.find("a").contents[0].replace("\n", "").lower())