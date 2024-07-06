from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./'+ name +'.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[1], top=position[1]) # 1 1
        self.speed = 0 # 0

    @abstractmethod
    def move(self):
        pass
