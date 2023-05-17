print("Television")
TVToggle = int(input("Choose 0-1: "))
if TVToggle == 0:
    print("The Television is off.")
elif TVToggle == 1:
    # create class named TV
    class TV:
        
    # current channel (1 to 120)
    # current volume level (1 to 7)
        def __init__(self, channel = [1, 120], volume = [1, 7]):
            self.channel = channel
            self.volume = volume

        # create two Class TV objects
        # construct a default TV object
        # create TestDriver program TestTV
        # indicate if on/off
        # returns channel
        # set new channel
        # gets volume level
        # set new volume level
        # increases channel number by 1
        # decreases channel number by 1
        # increases channel number by 1
        # decreases channel number by 1
        # print output

else:
    print("LOL")