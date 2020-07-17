import sys
import time
import keyboard
from garticrequester import GarticRequester
from garticfriendpage import GarticFriendPage

shouldStop = False

def onQuitKeyPressed():
    global shouldStop
    shouldStop = True

def extractRecentLoggedUsers(newList, oldList):
    for i in range(0, len(newList)):
        if oldList[0] == newList[i]:
            return newList[:i]

    return newList[:]

def main():
    # Checking if a username was passed ass the first parameter
    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        print("Username is missing. Pass the username as the first parameter of the program call")
        exit()

    keyboard.add_hotkey('ctrl+shift+q', onQuitKeyPressed)

    garticRequester = GarticRequester()

    timestamp = time.time() - 15
    oldList = []
    while not shouldStop:
        if time.time() - timestamp >= 15:
            timestamp = time.time()

            friendsPageRaw = garticRequester.getFriendsPageHtml(user, "1")
            friendsPage = GarticFriendPage(friendsPageRaw)

            if len(oldList) > 0:
                recentLoggedUsers = extractRecentLoggedUsers(friendsPage.friendsList, oldList)

                oldList = friendsPage.friendsList

                if len(recentLoggedUsers) > 0:
                    loggedUsersMsg = time.strftime('[%X %x]')

                    for user in recentLoggedUsers:
                        loggedUsersMsg = loggedUsersMsg + ' ' + user

                    print(loggedUsersMsg)

            else:
                oldList = friendsPage.friendsList

        time.sleep(.05)

if __name__ == "__main__":
    main()