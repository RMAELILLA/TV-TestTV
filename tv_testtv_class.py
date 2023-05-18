print(\
    """
         O         O
          \\     // 
           \\   //
            \\ // 
           /~~~~~\
           
    ,-------------------,
    | ,---------------, |
    | |               | |
    | |               | |
    | |               | |
    | |               | |
    | |_______________| |
    |___________________|
    |___________________|
    """)
print("TELEVISION")
# indicate if on/off
TVToggle = input("Choose 0-1: ")
if TVToggle == "0":
    TVoff = " The Television is off "
    print(TVoff.center(150, "#"))
elif TVToggle == "1":
    # create class named TV
    class TV:
    # current channel (1 to 120)
    # current volume level (1 to 7)
        def __init__(self, channel = 1, volume = 1):
            self.channel = channel
            self.volume = volume

        # create two Class TV objects
        # returns channel, volume
        def __str__(self):
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
        def channelUp(self):
            if self.channel < 120:
                self.channel += 1

        # decreases channel number by 1
        def channelDown(self):
            if self.channel > 1:
                self.channel -= 1

        # increases volume number by 1
        def volumeUp(self):
            if self.volume < 120:
                self.volume += 1

        # decreases volume number by 1
        def volumeDown(self):
            if self.volume > 1:
                self.volume -= 1

    # construct a default TV object
    TestTV = TV()

    # create TestDriver program TestTV
    while True:
        print(\
        """
             O         O
              \\     // 
               \\   //
                \\ // 
               /~~~~~\
           
        ,-------------------,
        | ,---------------, |
        | |               | |
        | |               | |
        | |               | |
        | |               | |
        | |_______________| |
        |___________________|
        |___________________|
        """)
        print("TELEVISION")
        print(TestTV) # print output
        
        try:
            tvTestTV = int(input(\
            """
            What do you wish to change? or do you want to exit?

            0 - Exit
            1 - Change Channel
            2 - Change Volume

            Your choice: 
            """))
            if tvTestTV == 0:
                print("The television is now off.")
                break
            elif tvTestTV == 1:
                channelNew = int(input("What channel number you want? : "))
                TestTV.setChannel(channelNew)
            elif tvTestTV == 2:
                volumeNew = int(input("What volume number you want range from 1-7? : "))
                TestTV.setVolume(volumeNew)
            else:
                print("cannot process your input choose only on 0-2. Try again")
        except ValueError:
            print("Try again, choose only from 0-2")

else:
    print("Sorry, try again.")