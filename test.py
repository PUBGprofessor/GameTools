from threading import Thread
from time import sleep
from threading import Thread
from params import *

p2 = PAGE(2)
p3 = PAGE(3)
print(p2.bag.getATK())
# command_key = 'o'
# # 定义一个实时获取键盘输入的程序
# def get_command():
#     global command_key  # 因为后续要对这个command_key 进行修改，所以这里需要声明成global
#     command_key = input()  # 获取输入
#     get_command()  # 获取下一次输入
#
# # 定义一个线程
# thd = Thread(target=get_command)  # 线程定义
# thd.start()  # 开启线程
#
# def control():
#     if command_key == 's':
#         print("stopped:Press c to start!")
#         stop_flag = True
#         while stop_flag:
#             if command_key == 'c':
#                 stop_flag = False
#                 print("continue")
#
# while 1:
#     control()
#     sleep(1)
#     print(1)