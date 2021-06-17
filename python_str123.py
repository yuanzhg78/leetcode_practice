#str.title()
str1 = 'nostalgia fly'
str2 = str1.title()
print(str2)

#检测字符串中是否包含子字符串 ：str.find(str, beg=0, end=len(string))
#end – 结束索引，默认为字符串的长度。
str1 = 'NOSTALGIA'
str2 = str1.find('no')
print(str2)

str1 = 'NOSTALGIA'
str2 = str1.find('AL',7)
print(str2)

#统计子字符串出现次数：str.count(sub, start= 0,end=len(string))
str1 = 'NOSTALGIAL'
str2 = str1.count('AL')
print(str2)

#index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内.
str1 = 'NOSTALGIAL'
str2 = str1.index('oL')
print(str2)
#注意index如果是没有的字符串会直接返回错误，find不会出错

#切片
test = 'hello world'
print(test[:])
print(test[:-1])
print(test[3:-2]) #lo wor

#字符串替换
#字符串中的 old（旧字符串） 替换成 new(新字符串)：str.replace(old, new[, max]) 次数是可以replace的最大次数
str1 = "This is a good new.That is so bad.It is a big apple.It is a dog."
str2 = str1.replace("is","was",3)
print(str2)

#字符串去除指定字符 注意只有头尾
#移除头尾指定字符（默认空格）：str.strip([chars])
str1 = '****       beauty   ********'
str2=str1.strip("*")
print(str2)
print(str2.strip())
#        beauty
# beauty

#字符串分割
#1、将字符串分割为列表：str.split(str=”“, num=string.count(str))
str1 = 'safdfg\nsfegewh\n12341y\n'
list1 = str1.split('\n',3)
print(list1)
#输出一个列表
#['safdfg', 'sfegewh', '12341y', '']

#判断
#以指定字符串开头：str.startswith(str, beg=0,end=len(string));
str1 = 'jefrewpflmspemg42sd'
print(str.startswith("w",5))
#True

#检测字符串是否由字母和数字组成：str.isalnum()
str1 = 'fewf125hreh'
print(str1.isalnum())

#检测字符串是否只由字母组成:str.isalpha()
str1 = 'sjdgnewombdfg'
print(str1.isalpha())

#检测字符串是否只由数字组成：str.isdigit()
str1 = '3141592653'
print(str1.isdigit())

#连接
#str.join(sequence) 将序列中的元素以指定的字符连接生成一个新的字符串
list1 = ['hels','sdfg','dsg','345']
dict1 = {'god':'sdf','dgg':'we','ewr':'435'}
tup1 = ('ty','rj','45')
s1 = {'we','34','12'}
print('-'.join(list1))
print('-'.join(dict1))
print('-'.join(tup1))
print('-'.join(s1))
#hels-sdfg-dsg-345
# god-dgg-ewr
# ty-rj-45
# 34-12-we


#sorted
n, k = [int(x) for x in input().split()]
E = [int(x) for x in input().split()]
W = [int(x) for x in input().split()]

W2 = []
for i in range(n):
    W2.append([i + 1, W[i]])  # 二维数组 [[序号，权值]]
W2 = sorted(W2, key=lambda x: (-x[1], x[0]))  # 按多条件多重排序
for i in range(n):
    W2[i][1] += E[i % 10]
W2 = sorted(W2, key=lambda x: (x[1], -x[0]), reverse=1)
for i in range(k):
    print(W2[i][0], end=' ')