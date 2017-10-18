import pygame

from settings import Settings
from  ship import  Ship
from pygame.sprite import Group
from  alien import Alien

import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )



    # 设置游戏题目
    pygame.display.set_caption("1")

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 设置游戏主循环

    bg_color = (230,230,230)
    # 开始游戏的主循环
    while True:

        """响应按键和鼠标事件"""
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        """更新子弹的位置，并删除已消失的子弹"""
        gf.update_bullets(bullets)

        """更新屏幕上的图像， 并切换到新屏幕"""
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()