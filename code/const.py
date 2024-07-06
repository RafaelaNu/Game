# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)

# M
MENU_OPTION = ('NEW GAME 1 P',
               'NEW GAME 2 P - COOPERATIVE',
               'NEW GAME 2 P - COMPETITIVE',
               'EXIT')

# W
WIN_WIDTH = 576  # 1080  # 576
WIN_HEIGHT = 324  # 900  # 324

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Level1Bg0': 4,  # 0
                'Level1Bg1': 1,  # 1
                'Level1Bg2': 2,  # 2
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Player1': 8,
                'Player2': 8,
                'Enemy1': 8,
                'Enemy2': 8,
                }

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w,
                 }

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s,
                   }

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_d,
                   }

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_a,
                    }
