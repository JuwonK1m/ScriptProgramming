from time import time

class StopWatch:
    def __init__(self):
        self.__startTime = time()
        
    def getStartTime(self):
        return self.__startTime
    
    def getStopTime(self):
        return self.__endTime
        
    def start(self):
        self.__startTime = time()
        
    def stop(self):
        self.__endTime = time()
        
    def getElapsedTime(self):
        return self.__endTime- self.__startTime