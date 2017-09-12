# _*_ coding:utf-8 _*_
from sys import argv

script, filename = argv

print ("We're going to erase %r." % filename)
#CTRL-C可以用来退出执行中的脚本
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

#这边用input作为一个中断程序执行的作用。
input("?")

print ("Opening the file...")
#打开文件，以写入模式操作
target = open(filename, 'w')

#因为使用了open的w模式，下面的truncate命令其实是多余的。  
#因为本身就会消除原来文件内的内容。简化代码，注释掉。 
#print "Truncating the file. Goodbye!"
#擦除文件原有的内容
#target.truncate()

#现在重新输入要写到文件中的内容
print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#将刚才用户输入的内容写到文件中去。
print ("I'm going to write these to the file.")

#原代码（在6行内输出）
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#在1行中输出
target.write("%s\n%s\n%s\n" % (line1, line2, line3)) 

#最后关闭文件
print ("And finally, we close it.")
target.close()


#附加练习：
#4找出为什么我们需要给 open 多赋予一个 'w' 参数。
#提示：open 对于文件的写入操作态度是安全第一，所以你只有特别指定以后，它才会进行写入操作。 
#因为默认open只能读取不能写入，所以要写入必须赋予'w'参数。