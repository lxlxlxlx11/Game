# Bullet类继承了我们从模块pygame.sprite中导入的Sprite类。
# 通过使用精灵，可将游戏中相关的元素编组，进而同时操作编组中的所有元素。
"""
子弹并非基于图像的，因此我们必须使用pygame.Rect()类从空白开始创建一个矩形。
创建这个类的实例时，必须提供矩形左上角的x坐标和y坐标，还有矩形的宽度和高度。
我们在（0,0）处创建这个矩形，但接下来的两行代码将其移到了正确的位置，
因为子弹的初始位置取决于飞船当前的位置。子弹的宽度和高度是从ai_settings中获取的。

将子弹的y坐标存储为小数值，以便能够微调子弹的速度。
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数点表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

