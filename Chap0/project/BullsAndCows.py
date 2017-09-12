# coding:utf-8
# 程序随机生成一个 20 以内的数字，用户有 10 次机会猜测
# 程序根据用户输入，给予一定提示（大了、小了、正确）
# 猜对或用完 10 次机会，游戏结束

# 增加判断是否为数字
# 增加提示还有多少次机会

import random

random_number = random.randint(1,20)

print("欢迎进入猜数字游戏！")
print("随意输入1~20以内的一个整数，如果和电脑生成的随机数一致，则表示你赢了，你只有10次猜数机会哟")

for count in range(0, 10):
	print("请输入一个数字,你还有%r次机会：" % (10-count))
	user_number = input(">>>")

	if user_number.isdigit() == False:
		print('你输入的不是数字，请重输')
	else:
		guess = int(user_number)
		if random_number < guess <= 20:
			print("你输入的数字大了")
		elif 0 < guess < random_number:
			print("你输入的数字小了")
		elif guess > 20:
			print("你输入的数字大于20超过范围了，请重输")
		elif guess < 1:
			print("你输入的数字小于1超过范围了，请重输")
		else:
			print("恭喜你，猜对了！")
			exit(0)
print("机会已经使用完了，正确的数字是：%r " % random_number)
