from tkinter import *




def init_window():
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

    Label(myWindow, text="请输入源文件夹路径", font=('Arial 12 bold'), width=20, height=5).pack(side='left')
    b1 = Button(myWindow, text='确定', bg="red", relief='raised', width=8, height=2)

    # b1.grid(row=0, column=0, sticky=W, padx=5, pady=5)




    #进入消息循环





    myWindow.mainloop()

if __name__ == '__main__':
    init_window()