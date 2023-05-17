print("Television")
# indicate if on/off
TVToggle = input("Choose 0-1: ")
if TVToggle == "0":
    print("The Television is off.")
elif TVToggle == "1":
    # create class named TV
    class TV:
    # current channel (1 to 120)
    # current volume level (1 to 7)
        def __init__(self, channel = 1, volume = 1):
            self.channel = channel
            self.volume = volume

        # create two Class TV objects
        # construct a default TV object
        def __str__(self):
            print(self.channel)
            print(self.volume)

        # create TestDriver program TestTV
        # returns channel, volume
        def getChannel(self):
            return f"Channel: {self.channel}\nVolume: {self.volume}"
        
        def getChannel(self):
            return self.channel
        
        # set new channel
        def setChannel(self, channel):
            if 1 <= channel <= 120:
                self.channel = channel

        # gets volume level
        def getVolume(self):
            return self.volume

        # set new volume level
        def setVolume(self, volume):
            if 1 <= volume <= 7:
                self.volume = volume
                
        # increases channel number by 1
        # decreases channel number by 1
        # increases channel number by 1
        # decreases channel number by 1
        # print output

else:
    print("LOL")