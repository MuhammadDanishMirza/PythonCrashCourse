import pygame
from class_settings import Setting
from ship_class import Ship
from event_check import check_events,update_screen


def run_game():
    
    # Initialize game and create a screen object.
    pygame.init()
    
    # Initialize pygame, settings, and screen object.
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("ALien Invasion")
    
    
    ship = Ship(screen)
    
    # Start the main loop for the game.
    while True:
        check_events(ship)
        ship.update()
        update_screen(setting,screen,ship)


run_game()
    
