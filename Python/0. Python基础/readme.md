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