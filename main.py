import sys
from garticrequester import GarticRequester
from garticfriendpage import GarticFriendPage
from garticprofilepage import GarticProfilePage

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
    friendsPageRaw = garticRequester.getFriendsPageHtml(user, "1")
    profileRaw = garticRequester.getProfileHtml(user)

friendsPage = GarticFriendPage(friendsPageRaw)
profile = GarticProfilePage(profileRaw)

print(user)
print("---")
print(profile.name)
print(profile.status)
print(profile.phrase)
print(profile.picture)
print("===")
print(friendsPage.friendsList)