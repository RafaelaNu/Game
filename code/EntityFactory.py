from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.const import WIN_WIDTH, WIN_HEIGHT
import random


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))  # 0 0
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))  # (WIN_WIDTH, 0)))
                    return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))  # (10, WIN_HEIGHT / 2))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 60))  # onde muda as posicoes das naves

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40)))

            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40 )))
