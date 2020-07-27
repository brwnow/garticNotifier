import argparse
from core.coreapplication import CoreApplication

def parseAppArgs():
    argsParser = argparse.ArgumentParser()

    argsParser.add_argument("-u", "--username", action='store', dest='username', required=True)
    argsParser.add_argument("-v", "--verbose", action='count', dest='logLevel', default=0)
    argsParser.add_argument("-w", "--watch-friends", action='store_true', dest="watchFriendList")
    argsParser.add_argument("-i", "--interval", action='store', dest='requestInterval', default=60)

    return argsParser.parse_args()

def main():
    CoreApplication(parseAppArgs()).runApplication()

if __name__ == "__main__":
    main()