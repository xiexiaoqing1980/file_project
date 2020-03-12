from tkinter import *


#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('File tool')
#设置窗口大小
width = 500
height = 500
#获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
myWindow.geometry(alignstr)
#设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=True, height=True)
L1 = Label(myWindow, text="请输入源文件夹路径", font=('Arial 8 bold'), width=20, height=1).pack(side='left')
src = Entry(myWindow, bd=5, width=30)
src.pack(side='left')
L2 = Label(myWindow, text="请输入目标文件夹路径", font=('Arial 8 bold'), width=20, height=10).pack(side='left')
target = Entry(myWindow, bd=5, width=30)
target.pack(side='left')

def click_confirm():

    src_value=src.get()
    target_value=target.get()
    condict=dict()
    condict["src_file_path"]=src_value
    condict["target_file_path"]=target_value
    print(condict)
    return  condict    #返回数值字典


    # b1.pack(row=0, column=0, sticky=W, padx=5, pady=5)


    #进入消息循环
b1 = Button(myWindow, text='确定', relief='raised', width=8, height=5,command=click_confirm())
b1.pack(side='bottom')
if __name__ == '__main__':

    myWindow.mainloop()


# def get_value(Entry):
    # value=Entry.get()
    # return value
