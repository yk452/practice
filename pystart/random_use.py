#-*-coding:utf-8-*-

#创建文件的名称不能与引入的模块名称一致，否则会提示如下错误：TypeError: 'module' object is not callable
import random

#random.random()用于生成一个0到1的随机符点数
for i in range(1,20):
    if(i<19):
        print (random.random(),i)
    else:
        print("结束产生随机数")

#random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: b <= n <= a。如果 a <b， 则 a <= n <= b
print(random.uniform(11,20))
print(random.uniform(9,3))
print("结束获取指定范围随机数")

#random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
print(random.randint(5,12))
print("结束获取指定范围整数")

#random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数
print(random.randrange(5,100,5))
print("结束获取指定范围按基数递增的随机整数")

#random.choice(sequence)，参数sequence表示一个有序类型，sequence在python不是一种特定的类型，list, tuple, 字符串都属于sequence
print(random.choice("张王李高孙牛马谢张"))
print(random.choice(["爱","轩","豪"]))
print(random.choice(("宇","伟","丽")))
print("结束从序列中获取随机元素")

#random.shuffle(x[, random])，用于将一个列表中的元素打乱
ks=[10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(ks)
print(ks)
print("结束列表元素打乱")

#random.sample(sequence, k)，从指定序列中随机获取指定长度的片断
ys=[21,22,23,24,25,26,27,28,29,30]
kw=random.sample(ys,4)
print(kw,"获取的指定片段")
print(ys,"random.sample方法不会改变原序列")


