#第一种方法
def lengthOfLongestSubstring(self, s):
    start = 0
    maxlen = 0
    hashtable = [-1 for i in range(256)]
    for i in range(len(s)):
        if hashtable[ord(s[i])] != -1:
            while start <= hashtable[ord(s[i])]:
                hashtable[ord(s[start])] = -1
                start += 1
        if i - start + 1 > maxlen: maxlen = i - start + 1
        hashtable[ord(s[i])] = i
    return maxlen
#第二种方法
def lengthOfLongestSubstring1(self, s):
    start = 0
    maxlen = 0
    dict = {}
    for i in range(len(s)):
        dict[s[i]] = -1
    for i in range(len(s)):
        if dict[s[i]] != -1:
            while start <= dict[s[i]]:
                dict[s[start]] = -1
                start += 1
        if i - start + 1 > maxlen: maxlen = i - start + 1
        dict[s[i]] = i
    return maxlen