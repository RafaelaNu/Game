from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./Summer4.png')  # ('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[10], top=position[10])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass
