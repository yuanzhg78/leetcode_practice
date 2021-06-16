class Solution:
    def solveEquation(self, equation):
        left, right = equation.split('=')
        if left[0] == '-':
            left = '0' + left
        if right[0] == '-':
            right = '0' + right
        left = left.replace('-','+-')
        right = right.replace('-', '+-')
        l_x, l_val = 0, 0
        r_x, r_val = 0, 0
        for num in left.split('+'):
            if 'x' in num:
                if num == 'x':
                    l_x += 1
                elif num == '-x':
                    l_x -= 1
                else:
                    l_x += int(num[:-1])
            else:
                l_val += int(num)
        for num in right.split('+'):
            if 'x' in num:
                if num == 'x':
                    r_x += 1
                elif num == '-x':
                    r_x -= 1
                else:
                    r_x += int(num[:-1])
            else:
                r_val += int(num)
        l_x = l_x - r_x
        r_val = r_val - l_val
        if l_x != 0 and r_val == 0:
            return "x=0"
        elif l_x != 0 and r_val != 0:
            return 'x=' + str(r_val//l_x)
        elif l_x == 0 and r_val == 0:
            return "Infinite solutions"
        elif l_x == 0 and r_val != 0:
            return "No solution"

if __name__ == "__main__":
    equation = "x+5-3+x=6+x-2"
    #pre = createTree(pre)
    #post=createTree(post)
    res=Solution().solveEquation(equation)
    print(res)
