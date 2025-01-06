from params import *

def build():
    # 打造
    p2 = PAGE(2)
    p3 = PAGE(3)
    while 1:
        # control()
        p3.toBag()
        p3.bag.toAlt("打造")
        p3.bag.toColumn("道具")
        p3.bag.toPage(2)
        p3.bag.getGrid(4, 4)
        # control()
        p3.bag.getGrid(5, 3)
        p3.bag.getGrid(5, 3)
        p3.bag.getGrid(5, 3)
        # break
        p3.bag.makeIt()
        p3.bag.toResult()
        try:
            ATK = p3.bag.getATK()
            print(ATK)
            if ATK >= 115:
                print('Down')
                break
        except ValueError:
            print("ValueError")
        # control()
        p3.bag.back()
        p3.back()
        p2.toPage()
        # control()
        p2.save()
        p3.toPage()
        p3.readFile()
        p3.toFile(1)

def strengthen():
    # 强化
    p2 = PAGE(2)
    p3 = PAGE(3)
    while 1:
        p3.toBag()
        p3.bag.toPage(2)
        p3.bag.getGrid(3, 3)
        p3.bag.toColumn("道具")
        p3.bag.toPage(2)
        p3.bag.getGrid(2, 5)
        p3.bag.getGrid(2, 5)
        p3.bag.makeIt()
        if isSameColor(getPixel((1438, 629)), color["黑色"]):
            print("强化失败")
        else:
            print("强化成功")
            break
        p3.bag.back()
        p3.back()
        p2.toPage()
        p2.save()
        p3.toPage()
        p3.readFile()
        p3.toFile(1)
