class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        #双指针法-原地压缩
        index = 0#新字符的下标，由于压缩后的字符串长度一定比之前的短，所以可以使用新的下表然后在原字串上更新
        lens = len(chars)
        i = 0#首字母指针
        while i < lens:
            j = i+1
            while j < lens and chars[j] == chars[i]:
                j += 1
            if j-i > 1:#相同的字符长度大于1，进行压缩：字符+数字
                chars[index] = chars[i]
                index += 1
                strs = str(j-i)
                for s in strs:
                    chars[index] = s
                    index += 1
            else:#相同字符的长度等于1，直接写字符，后不加数字
                chars[index] = chars[i]
                index += 1
            i = j
        return index#由于index指向的是压缩后字串的下标，所以可以直接返回index即可



class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        new = 0
        i = 0
        while i < len(chars):
            j = i + 1
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            if j - i > 1:
                chars[new] = chars[i]
                new += 1
                strs = str(j-i)
                for s in strs:
                    chars[new] = s
                    new += 1
            else:
                chars[new] = chars[i]
                new += 1
            i = j
        return new