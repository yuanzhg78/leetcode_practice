class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res
res=''
i=len(num1)-1
j=len(num2)-1
c=0
while i>=0 or j>=0:
    if i>=0:
     n1=int(num1[i])
    else:
        n1=0
    if j>=0:
        n2=int(num2[i])
    else:
        n2=0
    tmp=n1+n2+c
    c=tmp//10
    res=str(tmp%10)+res
    i-=1
    j-=1
return "1" + res if c else res
