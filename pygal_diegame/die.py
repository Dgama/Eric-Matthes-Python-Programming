from random import randint

class Die():
    """表示一个骰子"""
    def __init__(self,num_sides=6):
        """骰子面数"""
        self.num_sides=num_sides

    def roll(self):
        """投掷结果"""
        return randint(1,self.num_sides)