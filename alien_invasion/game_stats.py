class GameStats():
    #游戏统计数据

    def __init__(self,ai_settings):
        #初始化统计信息
        self.ai_settings=ai_settings
        self.reset_stats()
        self.game_active=False

        #不能初始化的得分记录
        self.highest_score=0

    def reset_stats(self):
        """初始化游戏期间的统计信息"""
        self.ship_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
