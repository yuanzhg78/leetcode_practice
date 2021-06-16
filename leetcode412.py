class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Approach #1
        answer = []
        for i in range(1,n+1):
            ans = ''
            if i % 3 == 0:
                ans = "Fizz"
                if i % 5 == 0:
                    ans += 'Buzz'
            elif i % 5 == 0:
                ans = "Buzz"
            else:
                ans = str(i)
            answer.append(ans)
        return answer
res=[]
for i in range(1,n+1):
    ans=''
    if i % 3 == 0:
        ans='Fizz'
        if i%5 == 0
            ans+='Buzz'
    elif i % 5 == 0:
        ans='Buzz'
    else:
        ans=str(i)
    res.append(ans)
return res