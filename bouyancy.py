# 이미지 출처: <a href="https://www.flaticon.com/kr/free-icons/" title="레크리에이션 아이콘">레크리에이션 아이콘 제작자: cube29 - Flaticon</a>
# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 860))
clock = pygame.time.Clock()
pygame.key.set_repeat(300, 30)
running = True



size = width, height = screen.get_size()
# image upload
background = pygame.image.load('images/ocean.png')
background = pygame.transform.scale(background, size)

diverimage = pygame.image.load("images/diver_forward_2.png")
diver = diverimage.get_rect()



shark1image = pygame.image.load("images/shark1.png")
shark1image = pygame.transform.scale(shark1image, (100, 100))
shark1 = shark1image.get_rect()

shark2image = pygame.image.load("images/shark2.png")
shark2image = pygame.transform.scale(shark2image, (130, 130))
shark2 = shark2image.get_rect()

shark3image = pygame.image.load("images/shark3.png")
shark3image = pygame.transform.scale(shark3image, (150, 150))
shark3 = shark3image.get_rect()

shark4image = pygame.image.load("images/shark4.png")
shark4image = pygame.transform.scale(shark4image, (170, 170))
shark4 = shark4image.get_rect()

shark5image = pygame.image.load("images/shark5.png")
shark5image = pygame.transform.scale(shark5image, (200, 200))
shark5 = shark5image.get_rect()


# shark 들
sharkimages = [shark1image, shark2image, shark3image, shark4image, shark5image]
sharks = [shark1, shark2, shark3, shark4, shark5]
num_sharks = len(sharks)

shark_regenerate = True
shark_i = random.randint(0, 4)
shark = sharks[shark_i]
shark.x = width
time = 0

shark_speed = [4, 5, 5.4, 6.1, 6.8]
diver_speed = 5
score = 0
scoreFont = pygame.font.SysFont("comicsans", 30)

prize_exist = False
prize = None
prizeimage = None


while running:
    screen.blit(background, (0, 0))

    time += 1
    print(time)
    if time % 1000 == 0:
        print("increase spped")
        for shark_speed_i in range(len(shark_speed)):
            shark_speed[shark_speed_i] += 0.7

    if time % 1500 == 0:
        diver_speed += 1

    if time % 700 == 0:
        prizeimage = pygame.image.load("images/prize.png")
        prizeimage = pygame.transform.scale(prizeimage, (200, 200))
        prize = prizeimage.get_rect()

        prize.x = random.randint(0, width)
        prize.y = random.randint(0, height)

        prize_exist = True


    if prize_exist and prize:
        screen.blit(prizeimage, prize)

        if prize.left < diver.centerx < prize.right and prize.top < diver.centery < prize.bottom:
            score += 100
            prize_exist = False
            prize = None
            prizeimage = None
    # prize_speed = [2,2]
    # if prize.right > width or prize.left < 0:
    #     prize_speed[0] = -prize_speed[0]
    # if prize.top < 0 or prize.bottom > height:
    #     prize_speed[1] = -prize_speed[1]
    #
    # prize.x += prize_speed[0]
    # prize.y += prize_speed[1]

    textScore = scoreFont.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(textScore, (10, 10))
    # prize = None

    if shark.left < diver.centerx < shark.right  and shark.top < diver.centery < shark.bottom:
        print("TOTAL SCORE: ", score)
        running = False

    if shark.x <= 0:
        shark_regenerate = True

    if shark_regenerate:
        print("Shark regenerate")
        shark_i = random.randint(0, 4)
        shark = sharks[shark_i]
        shark.x = width

        random_height = random.randint(0, height)
        shark.y = random_height
        shark_regenerate = False


    shark.x -= shark_speed[shark_i]
    event = pygame.event.poll()


    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            diverimage = pygame.image.load("images/diver_up_2.png")
            diver.top -= diver_speed
        if event.key == pygame.K_DOWN:
            diverimage = pygame.image.load("images/diver_down_2.png")
            diver.top += diver_speed
        if event.key == pygame.K_LEFT:
            diverimage = pygame.image.load("images/diver_backward_2.png")
            diver.left -= diver_speed
        if event.key == pygame.K_RIGHT:
            diverimage = pygame.image.load("images/diver_forward_2.png")
            diver.left += diver_speed
            # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE
    screen.blit(diverimage, diver)

    screen.blit(sharkimages[shark_i], shark)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
