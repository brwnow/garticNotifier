import sys
from bs4 import BeautifulSoup
from garticrequester import GarticRequester

if len(sys.argv) > 1:
    user = sys.argv[1]
else:
    user = ""

friendsReq = ""
content = ""

if len(user) == 0:
    print("No user defined")
    exit()
else:
    garticRequester = GarticRequester()
    content = garticRequester.getFriendsPageHtml(user, "1")

soup = BeautifulSoup(content, 'lxml')

for player in soup.find_all("div", class_="titulo"):
    print(player.find("a").contents[0].replace("\n", "").lower())