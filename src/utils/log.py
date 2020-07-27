logLevel = 0

def log(msg):
    if logLevel > 0:
        print(msg)
    else:
        pass

def setLogLevel(value):
    global logLevel
    logLevel = value