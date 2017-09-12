
#  ch0 给6个月前自己的python教程

## 1、初识Python

> **说明** 该教程所使用的是Python3，系统是MacOs。

> **提醒** 初学编程要习惯手打代码取代粘贴复制，要多运行代码排错，要多写注释说明代码意义便于复习。读万条代码不如写百行代码，从0到1，只需要动手写起来！

### 安装python3

Step1：官网下载[http://www.python.org](http://www.python.org) 下载合适的版本。

Step2：安装，完成后通过终端检查计算机上是否成功安装python3，在终端键入
> $ python3 -V

若显示出目前python的版本，则表示安装成功。

## 2、Python基础

### 2.1 在交互式环境中输入表达式

安装好python后，你既可以直接在item2中输入‘表达式’简单求值，也可以写.py文件，再使用命令行运行得出结果。

首先，来尝试直接在命令行中输入内容进行运算：


```python
2 + 3*6
```




    20




```python
(2 + 3)*6 
```




    30




```python
2 ** 8
```




    256




```python
23 // 7
```




    3




```python
23 % 7
```




    2



* 下表列出了python所有的数学操作符

|操作符|操作|例子|求值为|
|------|:------:|------:|------:|
|**|指数|2**3|8|
|%|取余数|22%8|6|
|//|整除/商数取整|22//8|2|
|/|除法|22/8|2.75|
| \* |乘法|3\*5|15|
|-|减法|5-2|3|
|+|加法|2+2|4|

* 运算优先级：括号、指数、乘、除、加、减。

### 2.2 整型、浮点型和字符串数据类型

* 常见数据类型

|操作符|例子|
|------|:------:|
|整型（int）|-2，-1，0，3|
|浮点型（float）|-1.25，-1.0，0.5|
|字符串（strs）|'a', 'hello!'|

* 整数运算结果仍然是整数，浮点数运算结果仍然是浮点数。
* 整数和浮点数混合运算的结果就变成浮点数。
* %是求余数符号，不是百分号。
* 整数除法算出来比实际小，是因为它将小数部分丢弃了，可以使用浮点数解决。

### 2.3 在变量中保存值

* “变量（variable）”只不过是用来只带某个东西的名字，程序员可以通过使用变量名让他们的程序读起来更像自然语言。

* 如果一个新值赋给变量，老值就被遗忘。

* 你可以给变量名取任何名字，只要它遵守以下规则：
1. 只能是一个词。
2. 只能包含字母、数字和下划线。
3. 不能以数字开头。

* 变量名是区分大小写的。

* 好的变量名描述了它包含的数据，具有描述性的名字有助于提高代码可读性。

让我们来看一些例子。

*程序1：*


```python
my_name = 'hujieying'
my_age = 25
my_height = 160.5 # cm
my_weight = 45 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print ("Let's talk about %s." % my_name)
print ("She's %d cm tall." % my_height)
print ("She's %d kg heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("She's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("Her teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get exactly right
print ("If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight))
```

    Let's talk about hujieying.
    She's 160 cm tall.
    She's 45 kg heavy.
    Actually that's not too heavy.
    She's got Brown eyes and Black hair.
    Her teeth are usually White depending on the coffee.
    If I add 25, 160, and 45 I get 230.


上面这段小程序，对很多变量进行了赋值，然后使用print()打印到屏幕上。代码中出现了%的使用，而且身高数据打印的也不对，这是怎么回事？别急，我们再看一段程序，再一一解释。

*程序2：*


```python
# this program says hello and asks for my name.

print('Hello world!')
print('What is your name?')
my_name = input()
print('It is good to meet you,' + my_name)
print('The length of your name is:')
print(len(my_name))
print('what is your age?')
my_age = input()
print('You will be ' + str(int(my_age) + 1) + 'in a year.')
print('How tall are you?')
my_height = input()
print('We are same, I am' + str(my_height) + 'cm.')
```

    Hello world!
    What is your name?
    hujieying
    It is good to meet you,hujieying
    The length of your name is:
    9
    what is your age?
    25
    You will be 26in a year.
    How tall are you?
    160.5
    We are same, I am160.5cm.


### 2.4 程序剖析

先根据上面的两个程序说明常用的一些函数和功能，后面章节更详细~

#### 2.4.1 注释


```python
# python中使用#来写注释。
# 如果看到关于ASCII编码的错误，那就在你的Python脚本的最上面加入下面这一行：
# -*- coding: utf-8 -*-  
```

#### 2.4.2 print()函数

* print()函数将括号内的字符串显示在屏幕上。在python2中，print使用时不使用括号，python3中做了改变。
* 使用print()，括号内没有任何东西，可以在屏幕上打印出空行。
* 程序1中，我们使用%d和%s占位来表示该处应该打印哪一个变量的值，然后在%后面的括号中，依次填入变量名即可。
* 程序2中，我们直接使用‘+’这个符号连接打印内容和变量。

#### 2.4.3 格式化字符

常见格式化字符如下：
> 
* %d --> 有符号整数，10进制
* %i --> 同%d
* %o --> 无符号整数，8进制
* %u --> 无符号整数，10进制
* %x --> 无符号整数，16进制
* %X --> 无符号整数，16进制大写字符
* %e --> 浮点数字，科学计数法
* %E --> 浮点数字，科学计数法，用E替代e
* %f --> 浮点数字，小数点
* %F --> 同%f
* %g --> 浮点数字，根据数字大小自动切换%e或%f
* %G --> 浮点数字，根据数字大小自动切换%E或%F
* %c --> 字符及其ASCII码(输出为字符或ASCII码对应的字符)
* %r --> 字符串 (采用repr()的显示)
* %s --> 字符串 (采用string()的显示)
* %% --> 输出一个百分号
> 

#### 2.4.4 input()函数

* 使用这个函数，可以要求用户输入合适的值给程序，然后进行后续运算。在程序1中，我们预设了值进行打印，而在程序2中，使用该函数赋值给变量进行打印。

#### 2.4.5 len()函数

* 你可以向len()函数传递一个字符串或包含字符串的变量，然后该函数求值为一个整型值，即字符串中字符的个数。见程序2

#### 2.4.6 str()、int()、float()函数

* str()、int()、float()函数将分别求值为传入值的字符串、整数和浮点数形式。


```python
str(0)
```




    '0'




```python
str(-3.14)
```




    '-3.14'




```python
int('42')
```




    42




```python
int('-99')
```




    -99




```python
int(1.25)
```




    1




```python
float('3.14')
```




    3.14




```python
float(10)
```




    10.0



## 3、控制流

### 3.1布尔值（Boolean）----> Ture or False

* 像其他值一样，布尔值也用在表达式中，并且可以保存在变量中。如果大小写不正确，或者试图使用True和False作为变量名，Python会报错。

如下程序所示：


```python
spam = True
spam
```




    True




```python
true
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-76-74d9a83219ca> in <module>()
    ----> 1 true
    

    NameError: name 'true' is not defined



```python
True = 2 + 2
```


      File "<ipython-input-77-5f87ef2f4024>", line 1
        True = 2 + 2
                    ^
    SyntaxError: can't assign to keyword



### 3.2 比较操作符

* “比较操作符”比较两个值，求值为一个布尔值。

>  
* !=   不等于
* ==   等于
* \>=    大于等于
* <=    小于等于
* \>    大于
* <   小于
>   

* 注意：整型或浮点型的值永远不会与字符串相等。
* <，>，<=，>=操作符仅用于整型和浮点型值。

* 注意‘==’和‘=’的区别！

### 3.3 布尔操作符 （and、or、not）

* 像比较操作符一样，它们将这些表达式求值为一个布尔值。
* 我们将使用这些字符来创建你需要记住的真值表。

|     NOT   |   真假 |
|----------|:---------:|
|not False  |  True|
|not True  | False|

|  OR   |   真假   |
|-------|:-------:|
|True or False|True|
|True or True|True|
|False or True|True|
|False or False|False|

|  AND  |   真假   |
|-------|:-------:|
|True and False| False|
|True and True|True|
|False and True|False|
|False and False|False|

|  NOT OR  |   真假   |
|-------|:-------:|
|not(True or False)|False|
|not(True or True)|False|
|not(False or True)|False|
|not(False or False)|True|

|  NOT AND  |   真假   |
|-------|:-------:|
|not(True and False)|True|
|not(True and True)|False|
|not(False and True)|True|
|not(False and False)|True|

|  !=  |   真假   |
|-------|:-------:|
|1!=0|True|
|1!=1|False|
|0!=1|True|
|0!=0|False

|  ==  |   真假   |
|-------|:-------:|
|1==0|False|
|1==1|True|
|0==1|False|
|0==0|True|

* 和算数操作符一样，布尔操作符也有操作顺序。在所有算数和比较操作符求值后，Python先求值not操作符，然后是and操作符，然后是or操作符。

### 3.4 控制流语句

#### 3.4.1 if、elif和else


```python
# coding:utf-8
people = 30
cars = 40
buses = 15

#如果满足条件车大于人，则输出
if cars > people:
	print ("We should take the cars.")
#或者如果车小于人，则输出
elif cars < people:
	print ("We shoud not take the cars.")
#或者前面两者都不满足，则输出
else:
	print ("We can't decide.")

if buses > cars:
	print ("That's too many buses.")
elif buses < cars:
	print ("Maybe we could take the buses.")
else:
	print ("We still can't decide.")
	
if people > buses:
	print ("Alright, let's just take the buses.")
else:
	print ("Fine, let's stay home then.")
	
if cars > people and buses > cars:
	print ("这是第一条")
else:
	print ("这是第二条")
```

    We should take the cars.
    Maybe we could take the buses.
    Alright, let's just take the buses.
    这是第二条


#### 3.4.2 while循环语句

* 只要while语句的条件为True，while子句中的代码就会执行。

* while语句看起来和if语句类似。不同之处是它们的行为。if子句结束时，程序继续执行if语句之后的语句。while子句结束时，程序执行跳回到while语句开始处。

下面的例子对比一下：


```python
spam = 0
if spam < 5:
    print('Hello, World.')
    spam = spam + 1
```

    Hello, World.



```python
spam = 0
while spam < 5:
    print('Hello, World.')
    spam = spam + 1
```

    Hello, World.
    Hello, World.
    Hello, World.
    Hello, World.
    Hello, World.


#### 3.4.3 break语句

* 有一个捷径，让执行提前跳出while循环子句。如果执行遇到break语句，就会马上退出while循环子句。在代码中，break语句仅包含break关键字。


```python
while True:
    print('Please type your name.')
    name = input()
    if name == "your name":
        break
print('Thank you!')
```

    Please type your name.
    hujieying
    Please type your name.
    hujieying
    Please type your name.
    hujieying
    Please type your name.
    your name
    Thank you!


#### 3.4.4 continue语句

* 像break语句一样，continue语句用于循环内部。如果程序执行遇到continue语句，就会马上跳回到循环开始处，重新对循环条件求值（这也是执行到达循环末尾时发生的事情）。


```python
while True:
    print('Who are you?')
    name = input()
    if name != 'hujieying':
        continue
    print('Hello, hujieying. What is the password?(It is a fish?)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
```

    Who are you?
    joe
    Who are you?
    anna
    Who are you?
    hujieying
    Hello, hujieying. What is the password?(It is a fish?)
    fish
    Who are you?
    hujieying
    Hello, hujieying. What is the password?(It is a fish?)
    swordfish
    Access granted.


**程序说明：**如果输入的名字不是hujieying，continue语句将导致程序执行跳回到循环开始处。如果执行通过if语句，用户被要求输入口令。如果输入的口令是swordfish，break语句运行，执行跳出while循环，打印Access granted。

#### 3.4.5 for循环和range()函数

* 如果你想让一个代码块执行固定次数，那就用range()函数吧~！
* 调用range()方法，最多传入3个参数，第一个参数是开始的值，第二个参数是上限，但不包含它，也就是循环停止的数字。第三个参数是“步长”，就是每次迭代后循环变量增加的值。


```python
print('My name is')
for i in range(5):
    print("Jimmy Five Times (" + str(i) + ")")
```

    My name is
    Jimmy Five Times (0)
    Jimmy Five Times (1)
    Jimmy Five Times (2)
    Jimmy Five Times (3)
    Jimmy Five Times (4)



```python
for i in range(0, 10, 2):
    print(i)
```

    0
    2
    4
    6
    8



```python
for i in range(5, -1, -1):
    print(i)
```

    5
    4
    3
    2
    1
    0


#### 3.4.6 导入模块

* python程序可以调用一组基本的函数，这称为“内建函数”，包括input()、len()等。
* python也包括一组模块，称为“标准库”。每个模块都是一个python程序，包含一组相关的函数，可以嵌入你的程序之中。如math模块有数学运算相关的函数，random模块有随机数相关的函数等等。
* 我们使用**import**语句导入模块。


```python
import random
for i in range(5):
    print(random.randint(1, 10))
```

    5
    4
    9
    6
    9


**程序说明：**random.randint()函数调用求值为传递给它的两个整数之间的一个随机整数，包含这两个整数（注意和range()函数对比一下，是否包含参数？）。因为randint()属于random模块，必须在函数名称之前先加上random，告诉python在random模块中寻找这个函数。

#### 3.4.7 用sys.exit()提前结束程序


```python
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('Your typed ' + response + '.')
```

    Type exit to exit.
    hujieying
    Your typed hujieying.
    Type exit to exit.
    exit



    An exception has occurred, use %tb to see the full traceback.


    SystemExit



    /Users/hujieying/anaconda/lib/python3.6/site-packages/IPython/core/interactiveshell.py:2889: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
      warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)


**程序说明：**该程序有一个无限循环，里面没有break语句。结束该程序的唯一方法就是用户输入exit，导致sys.exit()被调用。

## 4、函数

* 函数的一个主要目的就是将需要多次执行的代码放到一起。消除重复能够使程序更短、更易读、更容易更新。

### 4.1 def语句和参数，返回值和return语句

* def语句创建函数时，可是用return语句指定应该返回什么值。
* 如果在return语句中使用了表达式，返回值就是该表达式求值的结果。


```python
import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'this is five'
    elif answer_number == 6:
        return 'this is six'
    elif answer_number == 7:
        return 'this is seven'
    elif answer_number == 8:
        return 'this is eight'
    elif answer_number == 9:
        return 'this is nine'
    
r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)
```

    this is seven


**程序说明：**这里产生一个随机数赋值给函数，然后return出结果，这次程序运行结果表示，随机数是7，对应就输出了这句话。
最后3行也可以缩写为：print(get_answer(random.randint(1, 9)))。

### 4.2 None值

* 在python中有一个值称为None，它表示没有值。None是NoneType数据类型的唯一值。
* 如果你希望变量中存储的东西不会与一个真正的值混淆，这个没有值得的值就可能有用。有一个使用None的地方就是print()的返回值。print()函数在屏幕上显示文本，但它不需要返回任何值，这和len()或input()不同。但既然所有函数调用都需要求值为一个返回值，那么print()就返回None。


```python
spam = print('Hello!')
```

    Hello!



```python
None == spam
```




    True



* 在幕后，对于所有没有return语句的函数定义，Python都会在末尾加上return None。这类似于while或for循环隐式地以continue语句结尾。而且，如果使用不带值得return语句（也就是只有return关键字本身），那么就返回None。

### 4.3 关键字参数和print()

* 大多数参数是由它们在函数调用中的位置来识别的。例如：random.randint(1, 10)将返回1到10之间的一个随机整数。
* “关键字参数”是由函数调用时加在他们前面的关键字来识别的。感受一下下面几个程序就明白：


```python
print('Hello')
print('World')
```

    Hello
    World



```python
print('Hello', end='+')
print('World')
```

    Hello+World



```python
print('cats','dogs','mice')
```

    cats dogs mice



```python
print('cats','dogs','mice', sep=',')
```

    cats,dogs,mice


* print()函数自动在传入的字符串末尾添加了换行符，可以设置end关键字参数，将它变成另一个字符串
* 向print()传入多个字符串值，该函数会自动用一个空格分隔他们，可以使用sep关键字参数，替换。

### 4.4 局部和全局作用域

* 全局作用域中的代码不能使用任何局部变量；
* 但是，局部作用域可以访问全局变量；
* 一个函数的局部作用域中的代码，不能使用其他局部作用域中的变量；
* 如果在不同的作用域中，你可以使用相同的名字命名不同的变量。

#### 4.4.1 局部变量不能在全局作用域内使用


```python
def spam():
    eggs = 13
spam()
print(eggs)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-108-779c4a7c611b> in <module>()
          2     eggs = 13
          3 spam()
    ----> 4 print(eggs)
    

    NameError: name 'eggs' is not defined


#### 4.4.2 局部作用域不能使用其他局部作用域内的变量


```python
def spam():
    eggs = 99
    bacon()
    print(eggs)
    
def bacon():
    ham = 101
    eggs = 0
    
spam()
```

    99


#### 4.4.3 全局变量可以在局部作用域中读取


```python
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
```

    42
    42


#### 4.4.4 名称相同的局部变量和全局变量（这是应该避免的情况）


```python
def spam():
    eggs = 'spam local'
    print(eggs) #print 'spam local'
    
def bacon():
    eggs = 'bacon local'
    print(eggs) #print 'bacon local'
    spam()
    print(eggs) #print 'bacon local'
    
eggs = 'global'
bacon()
print(eggs) # print 'global'
```

    bacon local
    spam local
    bacon local
    global


### 4.5 global语句

* 如果需要在一个函数内修改全局变量，就使用global语句。


```python
def spam():
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)
```

    spam


**程序说明：**如果在函数的顶部有global eggs，就告诉python，“在这个函数中，eggs指的是全局变量，所以不要用这个名字创建一个局部变量。”

有4条法则，来区分一个变量是处于局部作用域还是全局作用域：

1、如果变量在全局作用域中使用（即在所有函数之外），它就是全局变量。

2、如果在一个函数中，有针对该变量的global语句，它就是全局变量。

3、否则，如果该变量用于函数中的赋值语句，它就是局部变量。

4、但是，如果该变量没有用在赋值语句中，它就是全局变量。

### 4.6 异常处理

* 错误可以由try和except语句来处理。可能出错的句子放在try子句中，如果发生错误，程序执行就转到接下来的except子句开始处。
* 注意区别下面两个程序写法不同而造成的结果不同。


```python
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error:Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
```

    21.0
    3.5
    Error:Invalid argument.
    None
    42.0



```python
def spam(divideBy):
        return 42 / divideBy
    
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
        print('Error:Invalid argument.')
```

    21.0
    3.5
    Error:Invalid argument.


## 5、列表

### 5.1 列表数据类型

#### 5.1.1 用下标取得列表中的单个值


```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
```




    'cat'




```python
spam[2]
```




    'rat'




```python
['cat', 'bat', 'rat', 'elephant'][3]
```




    'elephant'




```python
'hello ' + spam[0]
```




    'hello cat'




```python
spam[1000]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-12-61d5536a730b> in <module>()
    ----> 1 spam[1000]
    

    IndexError: list index out of range



```python
spam[1.0]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-13-bbdea97a156f> in <module>()
    ----> 1 spam[1.0]
    

    TypeError: list indices must be integers or slices, not float


* 列表包含列表，用多重下标访问：


```python
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0]
```




    ['cat', 'bat']




```python
spam[0][1]
```




    'bat'




```python
spam[1][4]
```




    50



#### 5.1.2 负数下标


```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1]
```




    'elephant'




```python
spam[-3]
```




    'bat'



#### 5.1.3 利用切片取得子列表


```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4]
```




    ['cat', 'bat', 'rat', 'elephant']




```python
spam[1:3]
```




    ['bat', 'rat']




```python
spam[0:-1]
```




    ['cat', 'bat', 'rat']




```python
spam[:2]
```




    ['cat', 'bat']




```python
spam[1:]
```




    ['bat', 'rat', 'elephant']




```python
spam[:]
```




    ['cat', 'bat', 'rat', 'elephant']



#### 5.1.4 用len()取得列表长度


```python
spam = ['cat', 'bat', 'rat', 'elephant']
len(spam)
```




    4



#### 5.1.5 用下标改变列表中的值


```python
spam = ['cat','bat','rat','elephant']
spam[1] = 'aardvark'
spam
```




    ['cat', 'aardvark', 'rat', 'elephant']




```python
spam[2] = spam[1]
spam
```




    ['cat', 'aardvark', 'aardvark', 'elephant']




```python
spam[-1] = 1234
spam
```




    ['cat', 'aardvark', 'aardvark', 1234]



#### 5.1.6 列表链接和复制


```python
[1, 2, 3] + ['A', 'B', 'C']
```




    [1, 2, 3, 'A', 'B', 'C']




```python
['X','Y','Z'] * 3
```




    ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']




```python
spam = [1, 2, 3]
spam = spam + ['A','B','C']
spam
```




    [1, 2, 3, 'A', 'B', 'C']



#### 5.1.7 用del语句从列表中删除值


```python
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
spam
```




    ['cat', 'bat', 'elephant']



### 5.2 使用列表

#### 5.2.1 列表用于循环


```python
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
```

    Index 0 in supplies is: pens
    Index 1 in supplies is: staplers
    Index 2 in supplies is: flame-throwers
    Index 3 in supplies is: binders


#### 5.2.2 in和not in操作符

* 确定一个值是否在列表中


```python
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name )
else:
    print(name + 'is my pet.')
```

    Enter a pet name:
    footfoot
    I do not have a pet named footfoot


#### 5.2.3 多重赋值技巧

* 用一行代码，用列表中的值为多个变量赋值，变量的数目和列表的长度必须严格相等。


```python
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition)
```

    fat
    black
    loud


### 5.3 增强的赋值操作


```python
spam = 42
spam += 1
spam
```




    43




```python
spam ='hello'
spam +=' world'
spam
```




    'hello world'




```python
bacon = ['zophie']
bacon *= 3
bacon
```




    ['zophie', 'zophie', 'zophie']



### 5.4 方法

#### 5.4.1 用index()方法在列表中查找值

* index()方法传入一个值，如果该值存在于列表中，就返回它的下标，如果不存在就报错；如果列表中存在重复的值，就返回它第一次出现的下标。


```python
spam = ['hello', 'hi', 'hey', 'how', 'hey']
spam.index('hello')
```




    0




```python
spam.index('hi hi')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-9-639d3ba966e8> in <module>()
    ----> 1 spam.index('hi hi')
    

    ValueError: 'hi hi' is not in list



```python
spam.index('hey')
```




    2



#### 5.4.2 用append()和insert()方法在列表中添加值


```python
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam
```




    ['cat', 'dog', 'bat', 'moose']




```python
spam.insert(1,'chicken')
spam
```




    ['cat', 'chicken', 'dog', 'bat', 'moose']



* 这两个是列表方法，只能在里列表上调用，不能在其他值上调用。


```python
eggs = 'hello'
eggs.append('world')
eggs
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-13-56cb3ef48bf0> in <module>()
          1 eggs = 'hello'
    ----> 2 eggs.append('world')
          3 eggs


    AttributeError: 'str' object has no attribute 'append'



```python
bacon = 12
bacon.insert(1, 'world')
bacon
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-14-9a21af367e97> in <module>()
          1 bacon = 12
    ----> 2 bacon.insert(1, 'world')
          3 bacon


    AttributeError: 'int' object has no attribute 'insert'


#### 5.4.3 用remove()方法从列表中删除值

* 传入一个值，它将从被调用的列表中删除；试图删除列表中不存在的值，会报错；如果该值在列表中出现多次，只有第一次出现的值会被删除。


```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam
```




    ['cat', 'rat', 'elephant']




```python
spam.remove('chicken')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-16-de76130db93f> in <module>()
    ----> 1 spam.remove('chicken')
    

    ValueError: list.remove(x): x not in list



```python
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
spam
```




    ['bat', 'rat', 'cat', 'hat', 'cat']



#### 5.4.4 用sort()方法将列表中的值排序

* 数值的列表或字符串的列表，能用sort()方法排序；也可以制定reverse关键字为True，按逆序排序；不能对既有数字又有字符串值得列表排序；对字符串排序时，使用“ASCII字符顺序”，而不是实际的字典顺序；如果需要按照普通字典顺序来排序，就在sort()方法调用时，将关键字参数key设置为str.lower。


```python
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam
```




    [-7, 1, 2, 3.14, 5]




```python
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam
```




    ['ants', 'badgers', 'cats', 'dogs', 'elephants']




```python
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort(reverse=True)
spam
```




    ['elephants', 'dogs', 'cats', 'badgers', 'ants']




```python
spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-22-a6b16ef533ed> in <module>()
          1 spam = [1, 3, 2, 4, 'Alice', 'Bob']
    ----> 2 spam.sort()
    

    TypeError: '<' not supported between instances of 'str' and 'int'



```python
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
spam
```




    ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']




```python
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort(key=str.lower)
spam
```




    ['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']



### 5.5 类似列表的类型：字符串和元组

* 字符串和列表实际上很相似，可以看做字符串是单个文本字符的列表。对列表的很多操作，也可以用于字符串：按下标取值、切片、用于for循环、用于len(),以及用于in和not in操作符。


```python
name = 'Zophie'
name[0]
```




    'Z'




```python
name[-2]
```




    'i'




```python
name[0:4]
```




    'Zoph'




```python
'Zo' in name
```




    True




```python
'z' in name
```




    False




```python
'p' not in name
```




    False




```python
for i in name:
    print('****' + i + '****')
```

    ****Z****
    ****o****
    ****p****
    ****h****
    ****i****
    ****e****


#### 5.5.1 可变和不可变数据类型

* 列表和字符串在一个重要的地方是不同的。列表是“可变的”数据类型，它的值可以添加，删除或改变。但是，字符串是“不可变的”，它不能被更改。
* “改变”一个字符串的正确方式，是使用切片和链接。即构造一个新的字符串从老的字符串那里复制一部分。


```python
name = 'Zophie a cat'
name[7] = 'the'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-36-4448876246c3> in <module>()
          1 name = 'Zophie a cat'
    ----> 2 name[7] = 'the'
    

    TypeError: 'str' object does not support item assignment



```python
name = 'Zophie a cat'
newname = name[0:7] + 'the' + name[8:12]
name
```




    'Zophie a cat'




```python
newname
```




    'Zophie the cat'




```python
eggs = [1, 2, 3]
eggs = [4, 5, 6]
eggs
```




    [4, 5, 6]



* 这里 eggs中的列表值并没有改变，而是整个新的不同的列表值，覆写了老的列表值。如果确实希望修改eggs中原来的列表，就需要使用del语句和append()方法。

#### 5.5.2 元组数据类型

* 元组与列表的区别：①元组输入时用圆括号()；②元组和字符串一样，是不可变的。
* 如果需要一个永远不会改变的值的序列，就使用元组。


```python
eggs = ('hello', 42, 0.5)
eggs[0]
```




    'hello'




```python
eggs[1:3]
```




    (42, 0.5)




```python
len(eggs)
```




    3



#### 5.5.3 用list()和tuple()函数来转换类型

* 函数list()和tuple()将返回传递给它们的值的列表和元组版本。


```python
tuple(['cat', 'dog', 5])
```




    ('cat', 'dog', 5)




```python
list(('cat','dog', 5))
```




    ['cat', 'dog', 5]




```python
list('hello')
```




    ['h', 'e', 'l', 'l', 'o']



### 5.6 引用

## 6、字典和结构化数据

### 6.1  字典数据类型

* 像列表一样，“字典”是许多值的集合。但不像列表的下标，字典的索引可以使用许多不同数据类型，不只是整数。字典的索引被称为“键”，字典输入时带花括号{}。


```python
mycat = {'size':'fat','color':'gray', 'disposition':'loud', 42:'red'}
mycat['size']
```




    'fat'




```python
mycat[42]
```




    'red'



#### 6.1.1 字典与列表

* 不像列表，字典中的表项是不排序的，就可以使用任意值作为键。


```python
birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'May 4'}

while True:
    print('Enter a name:(blank to quit)')
    name = input()
    if name =='':
          break
          
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
```

    Enter a name:(blank to quit)
    Alice
    Apr 1 is the birthday of Alice
    Enter a name:(blank to quit)
    Eve
    I do not have birthday information for Eve
    What is their birthday?
    Dec 5
    Birthday database updated.
    Enter a name:(blank to quit)
    Eve
    Dec 5 is the birthday of Eve
    Enter a name:(blank to quit)
    


#### 6.1.2 keys()、values()、items()方法 


```python
spam = {'color':'red','age':42}
for v in spam.values():
    print(v)
```

    red
    42



```python
for k in spam.keys():
    print(k)
```

    color
    age



```python
for i in spam.items():
    print(i)
```

    ('color', 'red')
    ('age', 42)


#### 6.1.3 get()方法

* get()方法有两个参数：要取得其值得键，以及如果该键不存在时，返回的备用值。如果不用get()就会报错。


```python
picnicItems = {'apples':5,'cups':2}
'I am bringing ' + str(picnicItems.get('cups',0)) + ' cups.'
```




    'I am bringing 2 cups.'




```python
'I am bringing ' + str(picnicItems.get('eggs',0)) + ' eggs.'
```




    'I am bringing 0 eggs.'




```python
'I am bringing ' + str(picnicItems['eggs'] + ' cups.'
```


      File "<ipython-input-17-60e8d4893205>", line 1
        'I am bringing ' + str(picnicItems['eggs'] + ' cups.'
                                                             ^
    SyntaxError: unexpected EOF while parsing



#### 6.1.4 setdefault()方法

* 给字典中的某个键设置一个默认值。下面程序第二次使用setdefault()的值没有被改变，因为spam变量已经有名为‘color’的键。


```python
spam = {'name':'carrie', 'age':25}
spam.setdefault('color', 'black')
```




    'black'




```python
spam
```




    {'age': 25, 'color': 'black', 'name': 'carrie'}




```python
spam.setdefault('color', 'white')
```




    'black'




```python
spam
```




    {'age': 25, 'color': 'black', 'name': 'carrie'}



## 7、字符串操作


```python

```


```python

```


```python

```


```python

```


```python

```
