import pygame

class Diver:
    def __init__(self, image_path, speed, screen_rect):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.screen_rect = screen_rect

    def move(self, direction):
        if direction == 'UP' and self.rect.top > 0:
            self.image = pygame.image.load("images/diver_up_2.png")
            self.rect.top -= self.speed
        elif direction == 'DOWN' and self.rect.bottom < self.screen_rect.height:
            self.image = pygame.image.load("images/diver_down_2.png")
            self.rect.top += self.speed
        elif direction == 'LEFT' and self.rect.left > 0:
            self.image = pygame.image.load("images/diver_backward_2.png")
            self.rect.left -= self.speed
        elif direction == 'RIGHT' and self.rect.right < self.screen_rect.width:
            self.image = pygame.image.load("images/diver_forward_2.png")
            self.rect.left += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
