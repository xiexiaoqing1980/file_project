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
frm.grid()
frm_l = Frame(frm,height=100)
frm_2 = Frame(frm,height=100)
frm_3 = Frame(frm,width=1)
frm_4 = Frame(frm,width=1)
frm_l.grid()
frm_2.grid()
frm_3.grid()
frm_4.grid()
v=[]
def click_checkbox():
    global selected_type        #声明为全局变量，可以在局部变量中修改值
    each_select=[]
    for state in v:
        if state.get() !="":
            each_select.append(state.get())
    selected_type = each_select

file_type_list=[".pdf",".docx",".doc",".txt",".img","jpg"]


frame1 = Frame(myWindow)
frame1.grid(row=0, column=0, sticky='w')  # sticky='w'指定了组件在单元格中靠左对齐

lb1_1= Label(frame1, text = '1、请选择用例识别方式: ')
lb1_1.grid()

# L1 = Label(frm_l, text="请选择要生成的文件类型（可多选）", font=('Arial 12 bold'), width=25, height=1).pack(side="left")
# L2 = Label(frm_2, text="请输入自定义文件类型", font=('Arial 12 bold'), width=20, height=10).pack(side="left")
# for type in file_type_list:
#     v.append(StringVar())
#     Checkbutton(frm_l, text=type, variable=v[-1],command=click_checkbox,onvalue=type,offvalue="").pack(side="left")
# file_type = Entry(frm_2,  width=30,bd=5)
# file_type.pack(side="left")
#
#
# L2 = Label(frm_3, text="请选择目标文件夹路径", font=('Arial 12 bold'), width=20, height=10).pack(side="left")
# target = Entry(frm_3,validate='focusout',width=25,bd=5)
# target.pack(side="left")
#
# b1 = Button(myWindow, text='确定', relief='raised', width=5, height=2).pack()
# Button(frm_3,text = "请选择文件的生成位置").pack(side="right")
#
# L2 = Label(frm_4, text="请输入需要生成的文件大小（MB）", font=('Arial 12 bold'), width=30, height=10).pack(side="left")
# file_size = Entry(frm_4, bd=5, width=30)
# file_size.pack(side="left")






if __name__ == '__main__':
    # deleteAllFiles("C:/Users/Administrator/Desktop/JSONView-for-Chrome-master")
    # dirs=os.listdir("D:/file_folder")
    # deleteAllFiles("D:/file_folder")
    # for file in dirs:
    # deleteAllFiles("D:/empty")
    #     print(file)
    # get_size("D:/file_folder/test.doc",1024)
    myWindow.mainloop()

