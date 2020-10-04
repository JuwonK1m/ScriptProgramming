class TV:
    def __init__(self):
        self.__channel = 1
        self.__volume = 1
        self.__on = False
        
    def turnOn(self):
        self.__on = True
        print("TV를 켰습니다.")
        
    def turnOff(self):
        self.__on = False
        print("TV를 껐습니다.")
        
    def setChannel(self, channel):
        if self.__on and 1 <= channel <= 100:
            self.__channel = channel
    
    def getChannel(self):
        return self.__channel
    
    def setVolume(self, volume):
        if self.__on and 0 <= volume <= 100:
            self.__volume = volume
            
    def getVolume(self):
        return self.__volume
    
    def channelUp(self):
        if self.__channel < 100:
            self.__channel += 1
            
    def channelDown(self):
        if self.__channel > 1:
            self.__channel -= 1
            
    def volumeUp(self):
        if self.__volume < 100:
            self.__volume += 1
        
    def volumeDown(self):
        if self.__volume > 0:
            self.__volume -= 1
        
tv = TV()

tv.turnOn()

tv.setChannel(63)
print(tv.getChannel())

tv.setVolume(20)
print(tv.getVolume())

tv.channelUp()
print(tv.getChannel())

tv.channelDown()
print(tv.getChannel())

tv.volumeUp()
print(tv.getVolume())

tv.volumeDown()
print(tv.getVolume())

tv.turnOff()