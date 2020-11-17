"""
创建一个编组（group），用于存储所有有效的子弹，以便能够管理发射出去的所有子弹。
这个编组将是pygame.sprite.Group类的一个实例；
pygame.sprite.Group类类似于列表，但提供了有助于开发游戏的额外功能。
在主循环中，使用这个编组在屏幕上绘制子弹，以及更新每颗子弹的位置；
"""


import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

# 供后面用来绘制游戏元素，如飞船和外星人。
# 我们还将让这个游戏响应用户输入、设置背景色以及加载飞船图像。

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # display.set_mode()返回的surface表示整个游戏窗口。我们激活游戏的动画循环后，每经过一次循环都将自动重绘这个surface。

    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船,一个用于存储子弹和一个外星人编组
    ship = Ship(ai_settings, screen)
    # 导入Ship类，并在创建屏幕后创建一个名为ship的Ship实例。
    # 必须在主while循环前面创建该实例，以免每次循环时都创建一艘飞船。

    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button,
                        ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb,
                              ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb,
                             ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                          play_button)

run_game()