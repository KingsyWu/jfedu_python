# coding=utf-8
# 京峰教育python课程第三次作业
# 密码验证程序 retry 3次: 验证一个文本里面的密码，如果正确返回，不正确重试3次
# 20170903 by zhu

# 验证密码
def verify_passwd(passwd, num):
    if num == 0:
        return
    user_passwd = "123456"
    if ((passwd == user_passwd)):
        print(passwd + "密码正确！\n")
    else:
        if num == 1:
            print(passwd + "密码错误，请联系管理员！\n")
            return 0
        else:
            print(passwd + "密码错误，你还有" + str(num - 1) + "次机会！")
            num -= 1
            verify_passwd(passwd, num)


def main():
    data = open('passwd.txt')
    count = 3 # 密码错误重试次数
    for line in data:
        passwd = line.strip('\n')
        verify_passwd(passwd, count)


if __name__ == '__main__':
    main()