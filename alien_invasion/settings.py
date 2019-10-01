class Settings():
    #存储游戏的所有参数设置

    def __init__(self):
        """初始化游戏静态设置"""
        # 初始化游戏的设置
        # 屏幕参数的设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        #飞船速度设置
        self.ship_limit=3

        #子弹设置
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=4

        #外星人的设置
        self.alien_drop_speed=10

        #加快游戏速度
        self.speed_up_factor=1.1
        self.score_speedup_factor=1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1

        #1为向右，-1为向左
        self.fleet_direction=1

        self.alien_points=50

    def increase_speed(self):
        self.ship_speed_factor*=self.speed_up_factor
        self.bullet_speed_factor*=self.speed_up_factor
        self.alien_speed_factor*=self.speed_up_factor
        self.alien_points=int(self.alien_points*self.score_speedup_factor)



