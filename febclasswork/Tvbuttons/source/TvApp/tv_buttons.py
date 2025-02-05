class Television:

    def __init__(self):
        self.__is_on = False
        self.__volume_level = 0
        self.__channel_level = 0
        self.__volume_store = 0

    def status(self):
        return self.__is_on

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def volume_up(self, number):
        if self.__is_on == True:
            self.__volume_level += number
        elif self.__is_on == False:
            self.__volume_level = 0
        elif self.__is_on ==True and self.__volume_level >= 100:
            self.__volume_level = 0


    def current_volume(self):
        return self.__volume_level

    def volume_down(self, number):
        if self.__is_on == False:
            self.__volume_level = 0
        elif self.__volume_level == 0:
            self.__volume_level = 0
        else:
            self.__volume_level -= number


    def channel_up(self, number):
        if self.__is_on == True:
            self.__channel_level += number
        elif self.__is_on == False:
            self.__channel_level = 0
        elif self.__is_on == True and self.__channel_level >= 100:
            self.__channel_level = 0

    def current_channel(self):
        return self.__channel_level

    def channel_down(self, number):
        if self.status() == False:
            self.__channel_level = 0
        elif self.__channel_level == 0:
            self.__channel_level = 0
        else:
            self.__channel_level -= number


    def mute(self):
        self.__volume_store = self.__volume_level
        self.__volume_level = 0

    def unmute(self):
        self.__volume_level = self.__volume_store



