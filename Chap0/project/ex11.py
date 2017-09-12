# -*- coding:utf-8 -*-
# python3的打印需要加上括号
print ("How old are you?")
# py3去掉了raw_input(), 使用input()
age = input()
print ("How tall are you?")
height = input()
print ("How much do you weight?")
weight = input()

# 这里的print也不要忘记加括号哦，否则就会错误提醒：TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'
print (("So, you're %r old, %r tall and %r heavy.") % (age, height, weight))

