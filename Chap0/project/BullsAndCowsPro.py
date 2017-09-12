# 开发升级版猜数字小游戏，实现以下功能：
# 程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
# 用户输入 4 位数进行猜测，程序返回相应提示
# 用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
# 用户猜测后，程序返回 A 和 B 的数量 比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
# 猜对或用完 10 次机会，游戏结束

#多个位数上的数字, 从同一数字序列中取出, 即可保证不相同

# coding:utf-8
import random

first_num = random.randint(1,9) #生成第1位数字，不为0


numbers = list(range(0,10)) #生成一个列表，包含0到9数字，相当于numbers = [0,1,2,3,4,5,6,7,8,9]
numbers.remove(first_num) #从numbers中把刚才生成的第1位数字移出
second_num = random.choice(numbers) #从新的列表中选出第2位数字


numbers.remove(second_num) #从numbers中把刚才生成的第2位数字移出
third_num = random.choice(numbers) #从新的列表中选出第3位数字


numbers.remove(third_num) #从numbers中把刚才生成的第3位数字移出
fourth_num = random.choice(numbers) #从新的列表中选出第4位数字

final_numbers = (first_num,second_num,third_num,fourth_num)
final_numbers2 = first_num*1000+second_num*100+third_num*10+fourth_num

for count in range(0,10):
	print('请输入一个四位数，首位不为0，且四个数字不重复：')
	print('你还有 %d 次机会' % (10-count))
	user_num = int(input(''))

	#用户输入的四位数为ijkl
	i = int(user_num/1000)
	j = int((user_num-i*1000)/100)
	k = int((user_num-i*1000-j*100)/10)
	l = user_num-i*1000-j*100-k*10
	guess_numbers = (i,j,k,l)

	A = 0
	B = 0

	#开始检查每个数字是否正确
	for i in range(0,4):
		#判断是否有相等数字
		if guess_numbers[i] in final_numbers:
			#判断是否位置相同，数和位置都相同则给A加1，否则数同位置不同则给B加1
			if (guess_numbers[i] == final_numbers[i]):
				A +=1
			else:
				B +=1
		#否则数不相同继续这个循环检查下一个数字
		else:
			continue

	#如果A等于4则表示才对
	if(A==4):
		print('你猜对了')
		exit(0)
	else:
		print(str(A)+'A'+str(B)+'B')

print('机会已经用完了，正确的数字是%s.' % str(final_numbers2))
