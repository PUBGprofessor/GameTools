from pyautogui import *
import numpy as np
import pytesseract
import PIL

window_A = (721, 211)
color = {"橙黄": (244, 147, 49), "白色": (255, 255, 255), "黑色": (0, 0, 0), "玄铁": (152, 152, 152)}

def getText(box, font_color=None):
    image = screenshot()
    # image = PIL.Image.open(r"C:\Users\xxx\Pictures\Screenshots\1.png")
    image = image.crop(box)
    # image.show()
    image = image.convert('RGB')
    tolerance = 20
    image = np.array(image)
    # print(image.shape)
    if font_color != None:
        image = 255*np.ones_like(image) * (np.mean(abs(image - font_color), axis=2, keepdims=True) < tolerance)

    new_image = PIL.Image.fromarray(image)
    new_image.convert('L')
    # new_image.show()
    config = '--psm 6 --oem 1'

    return pytesseract.image_to_string(new_image, config=config)
    # return pytesseract.image_to_string(image, lang='chi_sim')

def getTextCN(box, font_color=None):
    image = screenshot()
    # image = PIL.Image.open(r"C:\Users\xxx\Pictures\Screenshots\4.png")
    image = image.crop(box)
    # image.show()
    image = image.convert('RGB')
    tolerance = 45
    image = np.array(image)
    # print(image.shape)
    if font_color != None:
        image = 255*np.ones_like(image) * (np.mean(abs(image - font_color), axis=2, keepdims=True) < tolerance)

    new_image = PIL.Image.fromarray(image)
    new_image.convert('L')
    # new_image.show()
    # config = '--psm 6 --oem 1'

    # return pytesseract.image_to_string(new_image, config=config)
    return pytesseract.image_to_string(image, lang='chi_sim', config='--psm 13')

def getPixel(point):
    sleep(0.05)
    img = screenshot()
    return img.getpixel(point)

def isSameColor(c1, c2, tolerance=20):
    sum = 0
    for i in range(3):
        sum += abs(c1[i] - c2[i])
    return sum <= 3 * tolerance

class PAGE:
    def __init__(self, page_num):
        self.bag = BAG()
        self.num = page_num
        self.file = (1230, 614)
        self.file_gap = (400, 115)

    def save(self):
        sleep(2)
        moveTo(768, 1038)
        click()

    def toBag(self):
        sleep(0.1)
        moveTo(967, 1038)
        click()
        sleep(1)

    def back(self):
        sleep(0.1)
        moveTo(1457, 1038)
        click()

    def toPage(self):
        sleep(0.1)
        moveTo(340 + (self.num-1) * 300, 21)
        click()

    def readFile(self):
        # sleep(1)
        moveTo(1916, 514, duration=1)
        click()
        sleep(1)
        click()
        sleep(1)

    def toFile(self, num):
        sleep(0.1)
        r = (num-1) % 2
        c = (num-1) // 2
        moveTo(self.file[0] + r * self.file_gap[0], self.file[1] + c * self.file_gap[1])
        click()
        sleep(2)

class BAG:
    def __init__(self):
        self.ATK_R = {'loc': (469, 635), 'width': 47, 'height': 26}
        self.ATK_box = (window_A[0] + self.ATK_R['loc'][0],
                    window_A[1] + self.ATK_R['loc'][1],
                    window_A[0] + self.ATK_R['loc'][0] + self.ATK_R['width'],
                    window_A[1] + self.ATK_R['loc'][1] + self.ATK_R['height'])
        self.five_R = {'loc': (608, 583), 'width': 58, 'height': 24}
        self.five_box = (window_A[0] + self.five_R['loc'][0],
                        window_A[1] + self.five_R['loc'][1],
                        window_A[0] + self.five_R['loc'][0] + self.five_R['width'],
                        window_A[1] + self.five_R['loc'][1] + self.five_R['height'])
        self.column = {'装备': (1547, 427),
               '道具': (1658, 427),
               '时装': (1769, 427),
               '经书': (1880, 427),
                 }
        self.page = {1: (1787, 920), 2: (1845, 920), 3: (1902, 917)}
        self.grid_gap = (85, 89)
        self.first_grid = (1505, 522)
        self.make = (1214, 915)
        self.stren_result = (1047, 850)
        self.merge_result = (1184, 702)
        self.alt = {'强化': (861, 1062),
                    "合成": (980, 1062),
                    "打造": (1220, 1062)}
        self.goback = (2047, 257)
        self.five = "金木水火土"

    def grid(self, x, y):
        return self.first_grid[0] + self.grid_gap[0] * (x-1), self.first_grid[1] + self.grid_gap[1] * (y-1)

    def getGrid(self, x, y):
        # sleep(0.2)
        moveTo(self.grid(x, y), duration=0.2)
        click()

    def toPage(self, num):
        sleep(0.1)
        moveTo(self.page[num])
        click()

    def toResult(self):
        sleep(0.1)
        moveTo(self.stren_result)

    def toMerge(self):
        sleep(0.1)
        moveTo(self.merge_result)

    def back(self):
        sleep(0.1)
        moveTo(self.goback)
        click()

    def toAlt(self, str):
        # 切换到（强化、重铸...）
        sleep(0.1)
        moveTo(self.alt[str])
        click()

    def toColumn(self, str):
        sleep(0.1)
        moveTo(self.column[str])
        click()

    def makeIt(self):
        sleep(0.1)
        moveTo(self.make)
        click()

    def getATK(self):
        return int(getText(self.ATK_box, color["橙黄"]))

    def getFive(self):
        str1 = getTextCN(self.five_box, color["白色"])
        # print(str1)
        result = ''.join([char for char in self.five if char in str1])
        return result

class SHOP:
    def __init__(self):
        self.iron_point = [(window_A[0] + 464, window_A[1] + 332),
                           (window_A[0] + 464 + 151, window_A[1] + 332),
                           (window_A[0] + 464 + 151 + 158, window_A[1] + 332)]
        self.buy_point1 = (window_A[0] + 457, window_A[1] + 433)
        self.buy_gap = 153
        self.shop_point = (window_A[0] + 975, window_A[1] + 396)
        self.back_point = (window_A[0] + 1211, window_A[1] + 135)
    def toShop(self):
        sleep(0.1)
        moveTo(self.shop_point)
        click()

    def back(self):
        sleep(0.1)
        moveTo(self.back_point)
        click()

    def isIron(self, num):
        sleep(0.1)
        return isSameColor(getPixel(self.iron_point[num-1]), color["玄铁"], 1)

    def buy(self, num):
        sleep(0.1)
        moveTo(self.buy_point1[0] + self.buy_gap * (num-1), self.buy_point1[1])
        click()
