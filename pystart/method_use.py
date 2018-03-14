#-*-coding:utf-8-*-

def getKzResult(num):
    if(num%2 == 0 and num%3 == 0):
        print("yk2zx3")
        return
    if(num%2 == 0):
        print("yk2")
        return
    if(num%3 == 0):
        print("zx3")
        return
    print(num)

if __name__ == '__main__':
    minNum = input("请输入区间最小值:")
    maxNum = input("请输入区间最大值:")
    for num in range(int(minNum),int(maxNum)):
        getKzResult(num)

