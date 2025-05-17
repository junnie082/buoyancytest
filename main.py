from classes.Game import Game
import os
# 현재 위치 정의
current_path = os.path.dirname(__file__)
# 이미지 폴더 위치 정의
image_path = os.path.join(current_path, "images")

if __name__ == "__main__":
    game = Game(image_path)
    game.run()
