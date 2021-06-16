class Solution:
    def findKthNumber(self, n, k):
        k -= 1
        cur = 1
        while k > 0:
            step, first, last = 0, cur, cur + 1
            while first <= n:
                step += min(n + 1, last) - first
                first *= 10
                last *= 10
            if step <= k:
                cur += 1
                k -= step
            else:
                cur *= 10
                k -= 1
        return cur



prefix=1
p=1
count=0
cur=prefix
next=prefix+1
while cur<n:
    count+=min(n+1,next)-cur
    cur*=10
    next*=10
    if count<=k:
        prefix+=1
        k-=step
    else:
        prefix*=10
        k-=1
return prefix

class Solution:#final version  题解 第一个
    def findKthNumber(self, n: int, k: int) -> int:
            prefix=1
            p=1
            while(p<k):
                count=0
                cur=prefix
                net=prefix+1
                while cur<=n:
                    count+=min(n+1,net)-cur
                    cur*=10
                    net*=10
                if (p+count)<=k:
                        prefix+=1
                        p+=count
                else:
                        prefix*=10
                        p+=1
            return prefix