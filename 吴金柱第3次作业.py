# coding=utf-8
# jf-python第三次作业：密码验证程序 retry 3次: 验证一个文本里面的密码，如果正确返回，不正确重试3次
# by zhu
# ************************************************************************************************

def verity_passwd():
	for i in range(0,3):
		input_passwd = input("请输入密码：")
		user_passwd = "123456"
		if ((input_passwd == user_passwd)):
			print("密码正确！")
			return 0
		else:
			if i == 2:
				print("密码错误！次数超限，请联系管理员！")
			else:
				print("密码错误！请重新输入！")

verity_passwd()

