#打开文档
#c存三本书放到txt，放在pickle里边
#while循环，被文档一条一条的读出来
    #把没一条都给一个dict
        #判断dict[书名=我们要的]
            #判断dict[是否被借出]
               #如果没有被借出，就把他输出给写入到一个TXT函数里边
            #else 进行下一次判断
        #else进行下一次判断
#关闭所有文件
#把刚才的文档导出来
#放入一个GUI界面里边进行选择
#确认选择
#退出
import os
import sys
import pickle
book={
'ISNB':'swk1112', '书名':"毛泽东传2" ,'是否借出':1,'借出时间':20180511
}
pickle_file=open('book.pkl','wb')
pickle.dump(book,pickle_file)
pickle_file.close()
pickle_file=open('book.pkl','rb')
line=pickle.load(pickle_file)
dictk = line
if (dictk['书名'] == "毛泽东传2"):
        if (dictk['是否借出'] == 1):
            pickle_file = open('E:\\my_list.txt', 'ab')
            pickle.dump(dictk, pickle_file)
            pickle_file.close()
        else:
            print("no2_quit")#line = pickle.load(pickle_file)
else:
       print("no1") #line = pickle.load(pickle_file)
print("next")
pickle_file = open('E:\\my_list.txt', 'rb')
my_list2 = pickle.load(pickle_file)
#如果没有搜索到的要的，请重新输入，退出
#如果搜索到了
print("sd")
print(my_list2)
pickle_file .close()

#删除，退出
file = 'E:\\my_list.txt'
if os.path.exists(file):
    os.remove(file)
    print('yes')
else:
    print ('no such file:%s' % file)
