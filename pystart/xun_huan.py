#-*-coding:utf-8-*-

#正确
a=2
while a<28:
    print 'a 小于28，目前值为:',a
    a += 2
    if a%3 > 0:
        continue
    print 'a当前值是3的倍数',a
    if a%4 == 0:
        break

print "game over"


'''
#错误
a=2
while (a<12):
    print ('a 小于12，目前值为:',a)
    a += 2

print ("game over")
'''

b=3
while (b>2 and b<20):
    print "b当前值大于2小于20",b
    b+=2
else:
    print "b不再小于20"
