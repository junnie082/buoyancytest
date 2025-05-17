import pygame
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller 임시 경로
    except Exception:
        base_path = os.path.abspath(".")  # 개발 환경 경로
    return os.path.join(base_path, relative_path)

class Diver:
    def __init__(self, image_path, speed, screen_rect):
        self.image = pygame.image.load(resource_path(image_path))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.screen_rect = screen_rect

    def move(self, direction):
        if direction == 'UP' and self.rect.top > 0:
            self.image = pygame.image.load(resource_path("images/diver_up_2.png"))
            self.rect.top -= self.speed
        elif direction == 'DOWN' and self.rect.bottom < self.screen_rect.height:
            self.image = pygame.image.load(resource_path("images/diver_down_2.png"))
            self.rect.top += self.speed
        elif direction == 'LEFT' and self.rect.left > 0:
            self.image = pygame.image.load(resource_path("images/diver_backward_2.png"))
            self.rect.left -= self.speed
        elif direction == 'RIGHT' and self.rect.right < self.screen_rect.width:
            self.image = pygame.image.load(resource_path("images/diver_forward_2.png"))
            self.rect.left += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
