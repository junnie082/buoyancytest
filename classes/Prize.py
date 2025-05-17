import pygame
import random
import os


class Prize:
    def __init__(self, image_path, screen_rect):
        self.image = pygame.image.load(os.path.join(image_path, "prize.png"))
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect(
            x=random.randint(0, screen_rect.width - 200),
            y=random.randint(0, screen_rect.height - 200)
        )
        self.exist = True

    def draw(self, screen):
        if self.exist:
            screen.blit(self.image, self.rect)
