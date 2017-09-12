# coding:utf-8
print ("You enter a dark room with two doors. Do you go through door #1 or door #2 or door #3?")

door = input("> ")

if door == "1":
	print ("There's a giant bear here eating a cheese cake. What do you do?")
	print ("1. Take the cake.")
	print ("2. Scream at the bear.")
	
	bear = input("> ")
	
	if bear == "1":
		print ("The bear eats your face off. Good job!")
	elif bear == "2":
		print ("The bear eats your legs off. Good job!")
	else:
		print ("Well, doing %s is probably better. Bear runs away." % bear)
		
elif door == "2":
	print ("You stare into the endless abyss at Cthulhu's retina.")
	print ("1. Blueberries.")
	print ("2. Yellow jacket clothespins.")
	print ("3. Understading revolvers yelling melodies.")
	
	insanity = input("> ")
	
	if insanity == "1" or insanity == "2":
		print ("Your body survives powered by a mind of jello. Good job!")
	else:
		print ("The insanity rots your eyes into a pool of muck. Good job!")

elif door == "3":
	print ("你走进了一个空屋子，里面有两个盒子，你要选择第1个还是第2个呢？")
	print ("1. 这是一个铁盒子。")
	print ("2. 这是一个木盒子。")
	
	box = input("> ")
	
	if box == "1":
		print ("里面是一把钥匙，你可以开门出去。")
	elif box == "2":
		print ("里面什么都没有，你只有饿死在这里。")
	else:
		print ("你什么都没有选择。你只有饿死在这里。")

else:
	print ("You stumble around and fall on a knife and die. Good job!")
