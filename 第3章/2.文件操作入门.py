#读文件

#1.打开文件
file=open('./res/练习文件.txt','r',encoding='utf-8')
#2.读取文件
content=file.read()
print(content)
content=file.readlines()
for line in content:
    print(line.strip())
#3.关闭文件
file.close()

#1.打开文件 上面也可用这个方法释放资源
with open('./res/大狗诗.txt','w',encoding='utf-8') as file:
#2.写入文件
    file.write('  大狗诗\n')
    file.write('   大狗\n')
    file.write('大狗大狗叫叫叫\n')
    file.write('我嘴巴大大慢慢叫\n')
    file.write('大狗有此雅兴\n')
    file.write('你就先哈下吧\n')
#写文件