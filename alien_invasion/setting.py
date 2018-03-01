""" game setting """


class Setting():
    """ save game setting """

    def __init__(self):
        """ init game setting """
        # screen setting
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_speed_factor = 1
