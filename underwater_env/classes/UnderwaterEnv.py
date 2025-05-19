import pygame
import os

import numpy as np
import gymnasium as gym
from gymnasium import spaces

from underwater_env.classes.Diver import Diver
from underwater_env.classes.Prize import Prize
from underwater_env.classes.Shark import Shark

# 이미지 폴더 위치 정의
current_path = os.path.dirname(__file__)
parent_path = os.path.dirname(current_path)
image_path = os.path.join(parent_path, "images")

class UnderwaterEnv(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array'], "render_fps": 4}

    def __init__(self, render_mode = None):
        pygame.init()
        pygame.key.set_repeat(300, 30)

        self.image_path = image_path

        self.width, self.height = 1280, 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.background = pygame.image.load(os.path.join(self.image_path, "ocean.png"))
        self.background = pygame.transform.scale(self.background, self.screen.get_size())

        self.score = 0
        self.time = 0

        self.scoreFont = pygame.font.SysFont("Arial", 30)
        self.timeFont = pygame.font.SysFont("Arial", 30)

        self.diver = Diver(self.image_path, 5, self.screen.get_rect())
        self.shark_images = [pygame.image.load(os.path.join(image_path, f"shark{i}.png")) for i in range(1, 5)]
        self.shark = Shark(self.image_path, self.screen.get_rect())
        self.shark_regenerate = False
        self.prize = None

        self.observation_space = spaces.Dict(
            {
                "diver": spaces.Box(low=0, high=800, shape=(4,), dtype=np.int32),  # x, y, w, h
                "shark": spaces.Box(low=0, high=800, shape=(4,), dtype=np.int32),
            }
        )

        self._action_to_direction = {
            "NOTHING": 0,
            "UP": 1,
            "RIGHT": 2,
            "DOWN": 3,
            "LEFT": 4
        }

        self.action_space = spaces.Discrete(4)

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.running = True

        self.score = 0
        self.time = 0

        self.diver = Diver(self.image_path, 5, self.screen.get_rect())
        self.shark = Shark(self.image_path, self.screen.get_rect())
        self.shark_regenerate = False
        self.prize = None

    def _get_obs(self):
        return {
            "diver": np.array([self.diver.rect.x, self.diver.rect.y,
                               self.diver.rect.w, self.diver.rect.h], dtype=np.int32),
            "shark": np.array([self.shark.rect.x, self.shark.rect.y,
                               self.shark.rect.w, self.shark.rect.h], dtype=np.int32),
        }

    def _get_info(self):
        return {
            "score": self.score,
        }

    def step(self, action):
        # direction = self._action_to_direction[action]
        # print('direction', direction)
        # self.diver.move(direction)

        if action != "NOTHING":
            self.diver.move(action)
        self.shark.move()
        self.time += 1
        terminated = False

        if self.shark.rect.x <= 0:
            self.score += 10
            self.shark.regenerate()

        if self.time % 700 == 0:
            self.prize = Prize(self.image_path, self.screen.get_rect())
        if self.time % 700 == 0:
            self.shark.inc_speed()
        if self.time % 1000 == 0:
            self.diver.speed += 1

        if self.prize and self.prize.exist and self.prize.rect.collidepoint(self.diver.rect.center):
            self.score += 300
            self.prize.exist = False
            self.prize = None

        if self.shark.rect.collidepoint(self.diver.rect.center):
            terminated = True

        reward = self.score if terminated else 0
        observation = self._get_obs()
        info = self._get_info()

        self.render()

        return observation, reward, terminated, info

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
            self.score += 10
            self.shark_regenerate = True
        if self.shark_regenerate:
            self.shark.regenerate()
            self.shark_regenerate = False

        if self.time % 700 == 0:
            self.prize = Prize(self.image_path, self.screen.get_rect())
        if self.time % 700 == 0:
            self.shark.inc_speed()
        if self.time % 1000 == 0:
            self.diver.speed += 1

        self.check_collisions()

    def draw_ui(self):
        self.screen.blit(self.background, (0, 0))
        time_text = self.timeFont.render(f"Time: {self.time}", True, (255, 255, 255))
        score_text = self.scoreFont.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(time_text, (300, 10))
        self.screen.blit(score_text, (10, 10))

    def render(self):
        self.draw_ui()
        self.diver.draw(self.screen)
        self.shark.draw(self.screen)
        if self.prize and self.prize.exist:
            self.prize.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)

    def close(self):
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
