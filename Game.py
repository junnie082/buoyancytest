import pygame

from Diver import Diver
from Prize import Prize
from Shark import Shark


class Game:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(300, 30)

        self.width, self.height = 1280, 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.background = pygame.image.load("images/ocean.png")
        self.background = pygame.transform.scale(self.background, self.screen.get_size())

        self.score = 0
        self.time = 0

        self.scoreFont = pygame.font.SysFont("Arial", 30)
        self.timeFont = pygame.font.SysFont("Arial", 30)

        self.diver = Diver("images/diver_forward_2.png", 5, self.screen.get_rect())
        self.shark_images = [pygame.image.load(f"images/shark{i}.png") for i in range(1, 5)]
        self.shark = Shark(self.screen.get_rect())
        self.shark_regenerate = False
        self.prize = None

    def handle_events(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.diver.move('UP')
            elif event.key == pygame.K_DOWN:
                self.diver.move('DOWN')
            elif event.key == pygame.K_LEFT:
                self.diver.move('LEFT')
            elif event.key == pygame.K_RIGHT:
                self.diver.move('RIGHT')

    def check_collisions(self):
        if self.shark.rect.collidepoint(self.diver.rect.center):
            self.running = False
        if self.prize and self.prize.exist and self.prize.rect.collidepoint(self.diver.rect.center):
            self.score += 300
            self.prize.exist = False
            self.prize = None

    def update(self):
        self.time += 1
        self.shark.move()
        if self.shark.rect.x <= 0:
            self.shark_regenerate = True
        if self.shark_regenerate:
            self.shark.regenerate()
            self.shark_regenerate = False

        if self.time % 700 == 0:
            self.prize = Prize(self.screen.get_rect())
        if self.time % 1000 == 0:
            self.shark.speed += 0.7
        if self.time % 1500 == 0:
            self.diver.speed += 1
            self.score += 100

        self.check_collisions()

    def draw_ui(self):
        self.screen.blit(self.background, (0, 0))
        time_text = self.timeFont.render(f"Time: {self.time}", True, (255, 255, 255))
        score_text = self.scoreFont.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(time_text, (300, 10))
        self.screen.blit(score_text, (10, 10))

    def draw(self):
        self.draw_ui()
        self.diver.draw(self.screen)
        self.shark.draw(self.screen)
        if self.prize and self.prize.exist:
            self.prize.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)

    def game_over(self):
        font_large = pygame.font.SysFont("Arial", 80)
        font_small = pygame.font.SysFont("Arial", 50)
        text1 = font_large.render("Game OVER", True, (255, 0, 0))
        text2 = font_small.render(f"Score: {self.score}", True, (0, 0, 0))
        rect1 = text1.get_rect(center=(self.width // 2, self.height // 2 - 40))
        rect2 = text2.get_rect(center=(self.width // 2, self.height // 2 + 40))
        self.screen.blit(text1, rect1)
        self.screen.blit(text2, rect2)
        pygame.display.flip()
        pygame.time.delay(5000)
        pygame.quit()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
        self.game_over()
