# -*- coding:utf-8 -*-
# Take the maximun and minimun values of the list
# 20170816 by zhu@pycharm
# ***********************************************

# import re

# 通过内置函数获取最大最小值
def int_max_min(int_list):
    # 取列表最大值
    int_max = max(int_list)
    # 取列表最小值
    int_min = min(int_list)
    # 输出结果
    print("其中最大值是：" + str(int_max) + ", 最小值是：" +str(int_min) + "\n")

# 获取用户输入
def int_input():
    # 提示用户输入
    input_str = input("请输入正整数，以逗号隔开,q退出：\n")
    # 用户输入q，退出程序
    if input_str is "q":
        print("感谢使用！\n")
        exit()
    else:
        # 显示用户输入的内容
        print("你输入的正整数是：" + str(input_str))
        # 将用户输入的内容，以分割符间隔，由字符串string转为整型int，然后转化为列表list
        # input_list = [int(i) for i in input_str.split(',|;|:|\t|\0')]
        input_list = [int(i) for i in input_str.split(',')]
        #input_str2 = re.split(',|; |\*|\n',input_str)
        #input_list = [int(i) for i in input_str2]
        # print(list(input_list))
        # print("你输入的正整数是：" + str(input_list))
        # 返回列表input_list
        return input_list

if __name__ == '__main__':
    while 1:
        int_max_min(int_input())