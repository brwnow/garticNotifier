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
    __requestInterval = 60
    __user = None
    __algorithm = Algorithm()
    __garticRequester = GarticRequester()

    __mustWatchFriendList = False

    def __init__(self, args):
        keyboard.add_hotkey('ctrl+shift+q', onQuitKeyPressed)

        self.__user = args.username

        if args.requestInterval is not None:
            self.__requestInterval = int(args.requestInterval)

        if args.logLevel is not None:
            log.setLogLevel(args.logLevel)

        if args.watchFriendList is not None:
            self.__mustWatchFriendList = True

        # request timeout being set to 80% of request interval
        self.__garticRequester.setRequestTimeout(self.__requestInterval * .8)

    def runApplication(self):
        timestamp = time.time() - self.__requestInterval
        while not shouldStop:
            if time.time() - timestamp >= self.__requestInterval:
                timestamp = time.time()

                if self.__mustWatchFriendList == True:
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