class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for i in s.lower():
            if i.isalnum():
                a.append(i)
        return a == a[::-1]

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))

'''
i	Character	isalnum()	a (after append)
0	'a'	            True	['a']
1	' '	            False	['a']
2	'm'	            True	['a','m']
3	'a'         	True	['a','m','a']
4	'n'	            True	['a','m','a','n']
5	','	            False	['a','m','a','n']
6	' '         	False	['a','m','a','n']
7	'a'	            True	['a','m','a','n','a']
...	...	...	...
'''