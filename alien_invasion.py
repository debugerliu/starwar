import pygame

from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    # 设置一张画布
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_width))
    ship = Ship(ai_settings, screen)
    # 设置颜色
    # 设置标题
    pygame.display.set_caption('这是一个游戏')
    # 开始游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
