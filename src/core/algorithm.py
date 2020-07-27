class Algorithm:
    __lastFriendsList = []

    def __init__(self):
        pass

    def extractRecentLoggedUsers(self, newList):
        if len(self.__lastFriendsList) > 0:
            oldList = self.__lastFriendsList.copy()
            firstUnmatchingIndex = 0

            self.__lastFriendsList = newList

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
        else:
            self.__lastFriendsList = newList

            return []