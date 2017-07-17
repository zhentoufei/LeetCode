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

   见下面的代码

   ```
   def longestCommonPrefix(self, strs):
       """
       :type strs: List[str]
       :rtype: str
       """
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