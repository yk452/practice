#-*-coding:utf-8-*-

#初学变量赋值
counter = 500 #赋值整型变量
miles = 400.02 #浮点型
name = 'yangkan'

print counter
print miles
print name

#多个变量赋值
a=b=c=2
print a,b,c

a,b,c = 3,4,5
print a,b,c

#python中的标准数据类型：Numbers(数字)/String(字符串)/List(列表)/Tuple(元组)/Dictionary(字典)

str ="yang kan"

print str
print str[2:6]
print str[3:]
print str * 3
print str + "452"

#列表
list1=[87,'dong',30.4,'234','45',90,23]
list2=['zxx',26]

print list1
print list1[6]
print list1[2:5]
print list2 *3
print list1 + list2

#元组

tuple1=('1','true',874,'dajiu')
tuple2=(34,"dou")

print tuple1               # 输出完整元组
print tuple1[0]            # 输出元组的第一个元素
print tuple1[1:3]          # 输出第二个至第三个的元素
print tuple1[2:]           # 输出从第三个开始至列表末尾的所有元素
print tuple2 * 2           # 输出元组两次
print tuple1 + tuple2

#tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
#list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
#list[2] = 1000     # 列表中是合法应用

#字典

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print dict
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值