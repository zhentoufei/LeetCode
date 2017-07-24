### Python学习日常

```python
# coding:utf-8
# 根据条件过滤数据
from random import randint
import timeit

data = [randint(-10, 10) for _ in xrange(10)]


def function1():
    '''
    过滤器
    :return: 
    '''
    res = filter(lambda x: x > 0, data)


def function_2():
    '''
    列表解析，该方法别过滤器要快
    :return: 
    '''
    res2 = [x for x in data if x > 0]
    
print timeit.timeit(stmt=function1, number=1000000)
print timeit.timeit(stmt=function_2, number=1000000)
```

```python
# coding:utf-8
# 根据条件过滤数据
from random import randint

# 生成随机的字典
d = {x: randint(60, 100) for x in xrange(1, 21)}

# 过滤
dd = {k: v for k, v in d.iteritems() if v > 90}
```

### 2. 为元组中的每个元素命名，提高程序的可读性

   元组的好处是使用娇小的存储空间，而且访问速度比较快

```python
# coding:utf-8

from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('Jim', 16, 'male', 'xxx@xx.com')

print s
print s.age

s1 = Student(name='Tom', age=26, sex='male', email='aax@xx.com')
print s1
print s1.name
```

### 3. 统计序列中元素出现的频度

```python
# coding:utf-8
from random import randint

data = [randint(0, 20) for _ in xrange(30)]
diction = dict.fromkeys(data, 0)  # 以data作为索引， 0作为初始值

for x in data:
    diction[x] += 1
print diction
# 使用colleciton下的Counter对象
from collections import Counter

c2 = Counter(data).most_common(3)
print c2
```

### 4. 词频统计

```python
# coding:utf-8

import re
from collections import Counter

txt = open('test.txt', 'r')
c = Counter(re.split('\W+', txt))# 非字母的文件分割
```

### 5. 根据字典中的值得大小，对字典中的项排序

```python
# coding:utf-8
from random import randint

d = {x: randint(60, 100) for x in 'xyzabc'}
res1 = sorted(d)  # 根据key来排序

# 查看字典的可迭代对象
print iter(d)
print list(iter(d))

# 元组的比较 一般先比较第一个元素，在比较第二个元素
print (97, 'a') > (69, 'b')  # True
print (97, 'a') > (69, 'b')  # False

# 字典按照value排序的解决方案1
tmp = zip(d.values(), d.keys())  # 非迭代版本
tmp1 = zip(d.itervalues(), d.iterkeys())  # 迭代版本，节省内存空间
res2 = sorted(tmp)

# 字典按照value排序的解决方案2
# 查看字典的元素
print d.items()
# 排序
res3 = sorted(d.items(), key=lambda x: x[1])

# 解决方案3
import operator
res4 = sorted(d.items(), key=operator.itemgetter(1))
```

### 6. 快速找到字典中的公共键

   实际案例：西班牙足球甲级联赛，每轮球员进球统计

   第一轮：｛‘苏亚雷斯’：1，‘梅西’：2，‘本泽马’：1，‘C罗’：3...｝

   第二轮：｛‘苏亚雷斯’：2，‘C罗’：1，....｝

   ....

   统计出前N轮， 每场比赛都有进球的球员

```python
# coding:utf-8

from random import randint, sample

sample('asdfghj', 3)  # 表示从asdfghj中随机选择3个
sample('asdfghj', randint(3, 6))  # 从asdfghj随机选择随机个

# 生成进球球员
s1 = {x: randint(1, 4) for x in sample('asdfghj', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('asdfghj', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('asdfghj', randint(3, 6))}

# 一般的方法
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)

# 推荐的解决方案
# step1：使用字典的viewkeys()方法，得到一个字典keys的集合
# step2：使用map函数，得到字典的keys的集合
# step3：使用reduce函数，取出所有字典的keys的集合的交集
s1_keys = s1.viewkeys()
s2_keys = s2.viewkeys()
s3_keys = s3.viewkeys()
res = s1_keys & s2_keys & s3_keys  # 利用交集找到

# 下面我们使用map函数来实现
res1 = map(dict.viewkeys, [s1, s2, s3])  # 注意这里的viewkeys不带括号哦
res1 = reduce(lambda a, b: a & b, res1)
print res1
```

### 7. 如何让字典保持有序

   实际案例：某编程竞赛系统，对参赛选手编程解题进行及时，选手完成题目后，把该选手解题用时记录到字典中，一百年赛后按照选手名称查询成绩（答题用时越短，成绩越优秀）

   {'LiLei':(2,43), 'HanMeimei':(5,52), 'Jim':(1,39)......}

   比赛结束后，需要按照排名顺序一次打印选手成绩，如何实现？

```python
# coding:utf-8

# 在添加字典的时候，其实系统并不会帮助维护字典的顺序
d = {}
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 48)
for k in d: print k  # 打印出来后是和输入顺序不同的

# 解决方案 使用collection.OederedDict
# 以OrderDict替代内置字典Dict，一次将选手成绩存入OrderedDict

from collections import OrderedDict

d = OrderedDict()
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 48)
for k in d:
    print k  # 打印出来后是按照输入的顺序来写的

# 那么我们来实现响应的问题
from time import time
from random import randint
from collections import OrderedDict

d = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in xrange(8):
    raw_input()  # 阻塞程序的运行
    p = players.pop(randint(0, 7 - i))  # 每次随机选择出一个
    end = time()
    print i + 1, p, end - start
    d[p] = (i + 1, end - start)

print 
print '-'*20

for k in d:
    print k, d[k]
```

### 8. 如何实现用户的历史记录的功能(最多n条)？

   实际案例：很多程序都有浏览用户的历史记录的功能

   例如：

   浏览器可以查看最近访问过的网页

   视频播放器可以看最近播放过视频的文件

   Shell可以产看用户输入过的命令

   ......

   现在我们制作了一个简单的猜数字的小游戏，添加历史记录的功能，显示用户最近猜过的数字，如何实现？

```python
# coding:utf-8

from random import randint
from collections import deque

N = randint(0, 100)
history = deque([], 5)


def guess(k):
    if k == N:
        print 'right'
        return True
    if k < N:
        print '%s is less than N' % k
    else:
        print '%s is greater than N' % k
    return False


while True:
    line = raw_input('pls input a number: ')
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print list(history)
```
### 9. 如何实现可迭代对象和迭代器对象

   实践案例：某软件要求，从网络抓去各个城市气温信息，并依次显示：

   北京：15~20

   天津：17~22

   长春：12~18

   ......

   如果一次抓去所有城市天气再显示，显示第一个城市气温的时候有很高的延时，并且浪费存储空间，我们期望以“用时访问”的策略，并且能把所有城市气温封装到一个对象里面，可用for语句进行迭代，如何解决？

   解决方案：

   step1:实现一个迭代器对象WeatherIterator，next方法每次返回一个城市气温

   step2:实现一个可迭代对象WeatherIterable，\__iter__方法返回一个迭代器对象

```python
# coding:utf-8
from collections import Iterable, Iterator
import requests


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


if __name__=='__main__':
    for x in WeatherIterable([u'北京', u'上海']):
        print x
```

### 10. 如何使用生成器函数实现可迭代对象

​	实际案例：实现一个可迭代对象的类，它能迭代处给定范围内所有的素数：

​	pn = PrimeNumbers(1,30)

​	for k in pn:

​		print k

​	输出结果：2 3 5 7 11 13 17 19 23 29

​	解决方案：将该类的\__iter__方法实现生成器函数，每次yeild返回一个素数

```python
def f():
    print 'in f(), 1'
    yield 1

    print 'in f(), 2'
    yield 2

    print 'in f(), 3'
    yield 3


g = f()
# 下面的语句运行完毕，虽然通过yield输出了一个值，但是还保留了程序的运行状态，
# 那么在下次运行的时候会从2的地方输出
print g.next()

print g.next()
```

```python
class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False

        for i in xrange(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k


for x in PrimeNumbers(1, 100):
    print x
```

###11. 如何进行反向迭代以及如何实现反向迭代

​	如何实现一个连续浮点数发生器FloatRange(和xrange类似)，根据给定范围(start，end)和步进值(step)产生一些连续的浮点数，如迭代FloatRange(3.0,4.0,0.2)可产生序列：



正向：3.0 3.2 3.4 3.6 3.8 4.0

反向：4.0 3.8 3.6 3.4 3.2 3.0

```python
# coding:utf-8


###############################################################
l = [1, 2, 3, 4, 5]
l.reverse()  # 这种方法改变了原来的列表
l[::-1]  # 这种方法得到了一个与原来列表等大的方向列表

# 那么我们的解决方案是如下
reversed(l)  # 得到列表的反向迭代器，实际上调用了l.__reversed__()
iter(l)  # 得到列表的正向迭代器，实际上调用了l.__iter__()

for x in reversed(l):  # 实现了反向迭代
    print x


###############################################################


# 下面show出我的解决方案哦
class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


# 正向迭代
for x in FloatRange(1.0, 4.0, 0.5):
    print x

# 反向迭代
for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print x
```

###12. 如何进行反向迭代以及如何实现反向迭代
实际案例：有某个文件，我们想读取其中某范围的内容，如100~300行之间的内容，python中文本文件是刻碟带对象，我们是否可以使用类似列表切片操作的方式得到一个100~300行文件内容的生成器？

也就是说，使用下面的代码可以吗？
f=open('file')
f[100:300]

```python
# coding:utf-8

from itertools import islice

f = open('your_file.txt')

# 读取文件的所有的内容
lines = f.readlines()
print lines

for line in f:
    # 此时不会输出，因为在上面已经使用了print lines的操作，那么这个时候指针已经只向了最后的位置
    # 如果希望输出信息，那么我们就需要作如下的操作f.seek(0)
    print line

# 使用迭代器的方法迭代文件：
for line in islice(f, 100, 300):
    print line

for line in islice(f, 300):  # 读取到500行
    print line

for line in islice(f, 100, None):  # 从100，读取到最后
    print line

for line in islice(f, 100, -100):  
    # error,不能使用反向索引，
    # 因为这是一个迭代的过程，在此过程中明文件没有完全读取完毕，这时候不知道一共有多少行
    print line
```

```python
# coding:utf-8
from itertools import islice

# 注意点，初始化一个list
l = []
for i in xrange(15):
    l.append(i)
print l
# 此时的输出是0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

t = iter(l)
for x in islice(t, 5, 10):
    print x,
# 此时的输出是5 6 7 8 9

for x in t:
    print x
    # 此时的输出是10 11 12 13 14


# 所以在每次使用islice的时候都要重新申请一个对象，否则，在重新使用之前的iter处理过的对象的时候，会消耗之前的对象
```

###13 如何在一个for语句中迭代多个可迭代对象的？
实际案例
1. 某班同学期末考试成绩，语文，数学，英语，分别存储在3个列表中，同时迭代三个列表，计算每个学生的总分（并行）
2. 某年级有四个班级，某次考试每个班级的英语成绩分别是存储在4个列表中，依次迭代每个列表，统计全学年成绩高于90分人数（串行）
  **解决方案**：
  *并行*：使用内置函数zip，他能将多个刻碟带对象合并，每次迭代返回一个元组
  *串行*：使用标准库中的itertools.chain，他能将多个可迭代对象连接
```python
# coding:utf-8
# 针对问题1
from random import randint

chinese = [randint(60, 100) for _ in xrange(40)]
math = [randint(60, 100) for _ in xrange(40)]
english = [randint(60, 100) for _ in xrange(40)]

total = []
for i in xrange(len(math)):
    # 这么做的缺点是并不是所有的可迭代对象都支持引索操作，比如一个生成器
    total.append(chinese[i] + math[i] + english[i])

# 那么下面我们先看一些列子
# 例子1
print zip([1, 2, 3], ('a', 'b', 'c'))
# 输出：[(1,'a'), (2, 'b'), (3, 'c')]

# 例子2
print zip([1, 2, 3], ('a', 'b', 'c'), [5, 6, 7])
# 输出：[(1,'a'， 5), (2, 'b'， 6), (3, 'c'， 7)]

# 例子3
print zip([1, 2, 3], ('a', 'b'))
# 输出：[(1,'a'), (2, 'b')]

# 问题1的解决方案
for c, m, e in zip(chinese, math, english):
    total.append(c + m + e)
```
```python
# coding:utf-8
# 针对问题2
from itertools import chain
from random import randint
# 例子1
for x in chain([1, 2, 3, 4], ['a', 'b', 'c']):
    print x
    # 输出1 2 3 4 a b c


e1 = [randint(60, 100) for _ in xrange(40)]
e2 = [randint(60, 100) for _ in xrange(22)]
e3 = [randint(60, 100) for _ in xrange(33)]
e4 = [randint(60, 100) for _ in xrange(55)]
count = 0
for s in chain(e1, e2, e3, e4):
    if s > 90
        count += 1

print count
```