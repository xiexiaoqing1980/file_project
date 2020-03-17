import  os
from tkinter import *
from tkinter.filedialog import askdirectory
import gennerate_file as gen
from tkinter import messagebox

def deleteAllFiles(filePath):
    if os.path.exists(filePath):
        for dirpath ,dirnames,filenames in os.walk(filePath):
            for name in dirnames:
                print(os.path.join(dirpath,name))
            for name in filenames:
                print(os.path.join(dirpath,name))

def get_size(fullpath,fileSize):
    data_size=0
    with open(fullpath, 'a+') as fp:
        while data_size < fileSize:
            fp.write('1')  # 写入数字
            data_size = os.path.getsize(fullpath)

def test(firrst,second):
    return firrst-second


#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('File tool')
#设置窗口大小
width = 600
height = 600
#获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
myWindow.geometry(alignstr)
#设置窗口是否可变长、宽，True：可变，False：不可变
myWindow.resizable(width=True, height=True)

# 定义一个大的frame，定义在window上
frm=Frame(myWindow)
frm.pack()
frm_l = Frame(frm)
frm_r = Frame(frm)
frm_l.pack()
frm_r.pack()

L1 = Label(frm_l, text="请选择要生成的文件类型（可多选）", font=('Arial 12 bold'), width=30, height=1).pack(side="left")

L2 = Label(frm_r, text="请选择目标文件夹路径", font=('Arial 12 bold'), width=20, height=10).pack(side="left")
target = Entry(frm_r,validate='focusout')
target.pack(side="left")

b1 = Button(myWindow, text='确定', relief='raised', width=5, height=2).pack()
Button(frm_r, text = "请选择文件的生成位置").pack(side="right")







if __name__ == '__main__':
    # deleteAllFiles("C:/Users/Administrator/Desktop/JSONView-for-Chrome-master")
    # dirs=os.listdir("D:/file_folder")
    # deleteAllFiles("D:/file_folder")
    # for file in dirs:
    # deleteAllFiles("D:/empty")
    #     print(file)
    # get_size("D:/file_folder/test.doc",1024)
    myWindow.mainloop()

