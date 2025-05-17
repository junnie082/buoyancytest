import random
import pygame
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller 임시 경로
    except Exception:
        base_path = os.path.abspath(".")  # 개발 환경 경로
    return os.path.join(base_path, relative_path)

class Shark:
    def __init__(self, screen_rect, shark_images=None, speeds=None):
        self.screen_rect = screen_rect
        self.screen_width = screen_rect.width
        self.screen_height = screen_rect.height

        self.image_paths = shark_images or [
            "images/shark1.png",
            "images/shark2.png",
            "images/shark3.png",
            "images/shark4.png",
            "images/shark5.png",
        ]

        self.speeds = speeds or [5, 6, 7, 8, 9]
        self.image = None
        self.rect = None
        self.speed = 0
        self.reset()

    def reset(self):
        index = random.randint(0, len(self.image_paths) - 1)
        image_path = resource_path(self.image_paths[index])  # resource_path 적용
        base_speed = self.speeds[index]

        width = random.randint(80, 200)
        height = random.randint(80, 200)

        raw_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(raw_image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_width
        self.rect.y = random.randint(0, self.screen_height - self.rect.height)

        scale_factor = (150 / ((width + height) / 2))
        self.speed = max(3, int(base_speed * scale_factor))

    def move(self):
        self.rect.x -= self.speed

    def inc_speed(self):
        for speed in self.speeds:
            self.speeds[speed] += 1

    def regenerate(self):
        self.reset()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
