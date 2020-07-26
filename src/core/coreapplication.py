import sys
import time
import keyboard
import argparse
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
    __GARTIC_REQUESTS_INTERVAL = 60
    __user = None
    __algorithm = Algorithm()
    __garticRequester = GarticRequester()

    def __init__(self):
        keyboard.add_hotkey('ctrl+shift+q', onQuitKeyPressed)

    def enableFriendsActivityNotifications(self, userName):
        self.__user = userName

    def runApplication(self):
        # Checking if a username was passed ass the first parameter
        if len(sys.argv) > 1:
            self.__user = sys.argv[1]
        else:
            print("Username is missing. Pass the username as the first parameter of the program call")
            exit()

        timestamp = time.time() - self.__GARTIC_REQUESTS_INTERVAL
        while not shouldStop:
            if time.time() - timestamp >= self.__GARTIC_REQUESTS_INTERVAL:
                timestamp = time.time()

                self.__checkFriendsActivity()

            time.sleep(.05)

    def __checkFriendsActivity(self):
        log.log(self.__user + '\'s friends page 1 request attempt')
        friendsPageRaw = self.__garticRequester.getFriendsPageHtml(self.__user, "1")

        friendsPage = None

        if friendsPageRaw != None:
            log.log('Parsing ' + self.__user + ' first page of friends')
            friendsPage = GarticFriendPage(friendsPageRaw)
        else:
            log.log('Requesting ' + self.__user + ' friends page failed')
            return


        log.log('Detecting friends of ' + self.__user + ' that have logged since last check')
        recentLoggedUsers = self.__algorithm.extractRecentLoggedUsers(friendsPage.friendsList)

        if len(recentLoggedUsers) > 0:
            log.log('Friends login activity detected!')

            playsound("../media/sound/notification.wav")

            loggedUsersMsg = time.strftime('[%H:%M]')

            for friend in recentLoggedUsers:
                loggedUsersMsg = loggedUsersMsg + ' | ' + friend

            print(loggedUsersMsg)
        else:
            log.log('No friends activity')