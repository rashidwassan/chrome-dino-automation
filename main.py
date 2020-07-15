import pyautogui
from PIL import Image, ImageGrab
import time

def isCollide(data):

    # for cactus
    for i in range(425, 590):
        for j in range(420, 490):
            if data[i, j] > 150:
                pyautogui.keyDown('up')
                return

    # for birds
    # for i in range(460, 555):
    #     for j in range(370, 405):
    #         if data[i, j] > 150:
    #             pyautogui.keyDown('down')
    #             return


if __name__ == "__main__":
    time.sleep(3)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # # draw rectangle for cactus
        # for i in range(435, 590):
        #     for j in range(420, 490):
        #         data[i, j] = 150

        # # draw rectangle for birds
        # for i in range(460, 575):
        #     for j in range(370, 405):
        #         data[i, j] = 150

        # image.show()
        # break
