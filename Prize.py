import pygame
import random
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller 임시 경로
    except Exception:
        base_path = os.path.abspath(".")  # 개발 환경 경로
    return os.path.join(base_path, relative_path)

class Prize:
    def __init__(self, screen_rect):
        self.image = pygame.image.load(resource_path("images/prize.png"))
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect(
            x=random.randint(0, screen_rect.width - 200),
            y=random.randint(0, screen_rect.height - 200)
        )
        self.exist = True

    def draw(self, screen):
        if self.exist:
            screen.blit(self.image, self.rect)
