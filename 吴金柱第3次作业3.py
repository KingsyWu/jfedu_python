# coding=utf-8
# jf-python第三次作业：密码验证程序 retry 3次: 验证一个文本里面的密码，如果正确返回，不正确重试3次
# by zhu
# ************************************************************************************************

# 验证密码
def verity_passwd(passwd,num):
	if num == 0:
		return
	user_passwd = "123456" # 正确密码
	if ((passwd == user_passwd)):
		print(passwd + " 密码正确！")
		return 0
	else:
		if num ==1:
			print("密码错误，请联系管理员！\n")
		else:
			print(passwd + " 密码错误，还有" + str(num - 1) + "次机会！")
		num -= 1
		verity_passwd(passwd, num)

# 主程序
def main():
	count = 3 # 密码错误重试次数
	data = open('passwd.txt')
	for line in data:
		passwd = line.strip('\n')
		verity_passwd(passwd,count)

# 程序入口
if __name__ == '__main__':
	main()