class Settings():
    """储存所有设置的类"""

    def __init__(self):
        #屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)
        #飞船的设置
        self.ship_speed_factor = 3