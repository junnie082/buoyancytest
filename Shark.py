import random
import pygame

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
        image_path = self.image_paths[index]
        base_speed = self.speeds[index]

        width = random.randint(80, 200)
        height = random.randint(80, 200)

        raw_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(raw_image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_width  # self.screen_width은 int임
        self.rect.y = random.randint(0, self.screen_height - self.rect.height)

        scale_factor = (150 / ((width + height) / 2))
        self.speed = max(3, int(base_speed * scale_factor))

    def move(self):
        self.rect.x -= self.speed

    def regenerate(self):
        self.reset()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

