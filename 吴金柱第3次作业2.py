# coding=utf-8
# jf-python第三次作业：密码验证程序 retry 3次: 验证一个文本里面的密码，如果正确返回，不正确重试3次
# by zhu
# ************************************************************************************************

def verity_passwd():
	data = open('passwd.txt', 'r')
	user_passwd = "123456"
	for f in open('passwd.txt'):
		f = data.readline()
		print(f)
		if ((f == user_passwd)):
			print("密码正确！")
			return 0
		else:
			print("密码错误！请重新输入！")


verity_passwd()

