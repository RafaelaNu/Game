import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import Entity
from code.EntityFactory import EntityFactory
from code.const import COLOR_WHITE, MENU_OPTION


class Level:

    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # Opcao do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) # ADICIONA TODAS AS IMAGENS DE FUNDO
        self.entity_list.append(EntityFactory.get_entity('Player1'))  # ADICIONA O JOGADOR
        if menu_option in [MENU_OPTION[1],MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

    def run(self):
        pygame.mixer_music.load(f"./{self.name}.mp3")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Aqui eu desenho minhas entidades
                # self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE(10, 10))
                ent.move()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucid Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
