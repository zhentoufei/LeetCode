1. 输入的字符串要判断是不是字符串


2. 输入的字符串数组：判断是不是数组，判断数组元素是不是字符串

```
if not strs:
    return ""
for string in strs:
    if not string:
        return ""
```

3. 如果for循环里面写了个return，那么就要思考一下，是不是return完全了呢？for循环完毕了是不是要还有一个return

```
if not strs:
    return ""
for string in strs:
    if not string:
        return ""
for i in range(len(strs[0])):
    for string in strs[1:]:
        if i>=len(string) or string[i] != strs[0][i]:
            return strs[0][:i]
return strs[0]
```
4. 先看一段代码，关于数组的切片操作
```
>>a=['a']
>>print a[1:]
>>[] #可以看出这种切片操作如果索引不到不会报错，返回空
```

5. 链表，找到倒数第n个节点
```
dummy = ListNode(-1)
dummy.next = head
slow, fast = dummy, dummy

for i in xrange(n):
    fast = fast.next

while fast.next:
    slow, fast = slow.next, fast.next # 此时slow对应的就是要删除的节点
```

6. 一种两两合并的方式
```
if not lists:
    return None
left, right = 0, len(lists) - 1
while right > 0:
    if left >= right:
        left = 0
    else:
        lists[left] = mergeTwoLists(lists[left], lists[right])
        left += 1
        right -= 1
return lists[0]
```