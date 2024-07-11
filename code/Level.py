import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import EntityMediator
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityMediator import EntityMediator
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.const import C_WHITE, MENU_OPTION, EVENT_ENEMY, WIN_HEIGHT, C_CYAN, C_GREEN


class Level:

    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # Opcao do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # ADICIONA TODAS AS IMAGENS DE FUNDO
        self.entity_list.append(EntityFactory.get_entity('Player1'))  # ADICIONA O JOGADOR
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):
        pygame.mixer_music.load(f"./{self.name}.mp3")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            # For para desenhar todas as entidades
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Aqui eu desenho minhas entidades
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot
                    if shoot is not None:
                        self.entity_list.append(shoot)

                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 25))

                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health}| Score: {ent.score}', C_CYAN, (10, 45))

            # texto a ser printado na tela
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

            # Atualizar tela
            pygame.display.flip()

            # Verificar Relacionamentos de Entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # Conferir Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucid Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
