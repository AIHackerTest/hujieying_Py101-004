# 希望系统生成一个包含4位数字的列表，用户输入的也转化成一个列表。
import random

num = random.sample(range(10),4)
while num[0] == 0:
	num = random.sample(num, 4)

num_list = [str(num[0]),str(num[1]),str(num[2]),str(num[3])]
random_num = str(num[0])+str(num[1])+str(num[2])+str(num[3])

for count in range(0,10):
	print('请输入一个四位数，首位不为0，且四个数字不重复：')
	print('你还有 %d 次机会' % (10-count))
	user_num = list(input('>>>'))

	A = 0
	B = 0

	for i in range(0,4):
		if user_num[i] in num_list: #判断是否有相等数字
			if (user_num[i] == num_list[i]): #判断是否位置相同，数和位置都相同则给A加1，否则数同位置不同则给B加1
				A +=1
			else:
				B +=1
		else: #否则数不相同继续这个循环检查下一个数字
			continue

	if(A==4):
		print('你猜对了')
		exit(0)
	else:
		print(str(A)+'A'+str(B)+'B')

print('机会已经用完了，正确的数字是%s.' % random_num)
