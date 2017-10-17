import pygame

from settings import Settings
from  ship import  Ship
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

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 设置游戏主循环

    bg_color = (230,230,230)
    # 开始游戏的主循环
    while True:

        """响应按键和鼠标事件"""
        gf.check_events(ship)
        ship.update()
        """更新屏幕上的图像， 并切换到新屏幕"""
        gf.update_screen(ai_settings, screen, ship)

run_game()