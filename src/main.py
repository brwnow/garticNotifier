import sys
import time
import keyboard
from garticrequester import GarticRequester
from garticfriendpage import GarticFriendPage
from playsound import playsound
import log

shouldStop = False

def onQuitKeyPressed():
    global shouldStop
    shouldStop = True

def extractRecentLoggedUsers(newList, oldList):
    firstUnmatchingIndex = 0

    lenOfSmallerList = min(len(oldList), len(newList))
    while firstUnmatchingIndex < lenOfSmallerList:
        if oldList[firstUnmatchingIndex] != newList[firstUnmatchingIndex]:
            break
        else:
            firstUnmatchingIndex += 1

    if firstUnmatchingIndex == lenOfSmallerList:
        return []

    for i in range(firstUnmatchingIndex + 1, len(newList)):
        if oldList[firstUnmatchingIndex] == newList[i]:
            return newList[firstUnmatchingIndex:i]

    return newList[firstUnmatchingIndex:]

def main():
    GARTIC_REQUESTS_INTERVAL = 60 # in seconds
    user = ""

    # Checking if a username was passed ass the first parameter
    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        print("Username is missing. Pass the username as the first parameter of the program call")
        exit()

    keyboard.add_hotkey('ctrl+shift+q', onQuitKeyPressed)

    garticRequester = GarticRequester()

    timestamp = time.time() - GARTIC_REQUESTS_INTERVAL
    oldList = []
    while not shouldStop:
        if time.time() - timestamp >= GARTIC_REQUESTS_INTERVAL:
            timestamp = time.time()

            log.log(user + '\'s friends page 1 request attempt')
            friendsPageRaw = garticRequester.getFriendsPageHtml(user, "1")

            friendsPage = None

            if friendsPageRaw != None:
                log.log('Parsing ' + user + ' first page of friends')
                friendsPage = GarticFriendPage(friendsPageRaw)
            else:
                log.log('Requesting ' + user + ' friends page failed')
                continue

            if len(oldList) > 0:
                log.log('Detecting friends of ' + user + ' that have logged since last check')
                recentLoggedUsers = extractRecentLoggedUsers(friendsPage.friendsList, oldList)

                oldList = friendsPage.friendsList

                if len(recentLoggedUsers) > 0:
                    log.log('Friends login activity detected!')

                    playsound("media/sound/notification.wav")

                    loggedUsersMsg = time.strftime('[%X]')

                    for friend in recentLoggedUsers:
                        loggedUsersMsg = loggedUsersMsg + ' | ' + friend

                    print(loggedUsersMsg)
                else:
                    log.log('No friends activity')

            else:
                log.log('Storing current friends list order for further login detection')
                oldList = friendsPage.friendsList

        time.sleep(.05)

if __name__ == "__main__":
    main()