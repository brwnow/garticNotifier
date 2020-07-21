import sys
import time
import keyboard
from playsound import playsound

from utils import log
from core.algorithm import Algorithm
from requests.garticrequester import GarticRequester
from requests.garticfriendpage import GarticFriendPage

shouldStop = False

def onQuitKeyPressed():
    global shouldStop
    shouldStop = True

class CoreApplication:
    def __init__(self):
        pass

    def runApplication(self):
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

        algorithm = Algorithm()
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
                    recentLoggedUsers = algorithm.extractRecentLoggedUsers(friendsPage.friendsList, oldList)

                    oldList = friendsPage.friendsList

                    if len(recentLoggedUsers) > 0:
                        log.log('Friends login activity detected!')

                        playsound("../media/sound/notification.wav")

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