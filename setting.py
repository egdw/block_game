# 游戏参数设置类
class Settings():
    def __init__(self):
        # 屏幕宽度
        self.screen_width = 1200
        # 屏幕高度
        self.screen_height = 800
        # 屏幕背景
        self.screen_bg = (230, 230, 230)
        # 控制器的速度
        self.controler_speed = 15
        # 控制器的宽度
        self.controller_width = 150
        # 控制器的高度
        self.controller_height = 15

        # 球的速度
        self.ball_speed = 3
        # 球得宽度
        self.ball_width = 10
        # 球的高度
        self.ball_height = 10
        # 球的颜色
        self.ball_color = (0, 0, 0)

        # 砖块的宽度
        self.block_width = 30
        # 砖块的高度
        self.block_height = 30