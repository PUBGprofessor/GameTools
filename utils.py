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
        p3.bag.getGrid(4, 3)
        p3.bag.toColumn("道具")
        p3.bag.toPage(3)
        p3.bag.getGrid(2, 1)
        p3.bag.getGrid(2, 1)
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

def buyIron():
    def stop(num, flag, count):
        if num == flag:
            return num, count + 1
        else:
            return num, 0

    s = SHOP()
    s.toShop()
    flag = 0
    count = 0  # 连续buy(n)的次数，过多说明没有购买次数了
    while count < 20:
        if s.isIron(3):
            flag, count = stop(3, flag, count)
            s.buy(3)
            continue
        if s.isIron(2):
            flag, count = stop(2, flag, count)
            s.buy(2)
            continue
        if s.isIron(1):
            flag, count = stop(1, flag, count)
            s.buy(1)
            continue
        count = 0
        s.back()
        s.toShop()
    print("Down.")

def merge():
    # 合成
    p2 = PAGE(2)
    p3 = PAGE(3)
    while 1:
        p3.toBag()
        p3.bag.toAlt("合成")
        p3.bag.toPage(3)
        p3.bag.getGrid(1, 1)
        p3.bag.toColumn("道具")
        p3.bag.toPage(2)
        p3.bag.getGrid(3, 5)
        p3.bag.getGrid(3, 5)
        p3.bag.makeIt()
        p3.bag.toMerge()
        result = p3.bag.getFive()
        print(result)
        if result == "金木":
            print("Down.")
            break
        p3.bag.back()
        p3.back()
        p2.toPage()
        p2.save()
        p3.toPage()
        p3.readFile()
        p3.toFile(1)
