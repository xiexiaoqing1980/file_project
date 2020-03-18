from tkinter import *
from tkinter.filedialog import askdirectory
import gennerate_file as gen
from tkinter import messagebox



#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('File Generator')
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
frame1=Frame(myWindow)
frame1.grid(row=0, column=0, sticky='w')
# frm_r = Frame(frm)
L1 = Label(frame1, text="1、 * 请选择要生成的文件类型（可多选）", font=('Arial 10 bold'),padx = 0)
L1.pack(anchor="nw")

file_type_list=[".pdf",".docx",".doc",".txt",".img",".png",".jpg",".exe"]
selected_type=[]
v=[]          #状态数组

def click_checkbox():
    global selected_type        #声明为全局变量，可以在局部变量中修改值
    each_select=[]
    for state in v:
        if state.get() !="":
            each_select.append(state.get())
    selected_type = each_select

for type in file_type_list:
    v.append(StringVar())
    Checkbutton(frame1, text=type, variable=v[-1],command=click_checkbox,onvalue=type,offvalue="").pack(side="left")



frame2=Frame(myWindow)
frame2.grid(row=1, column=0, sticky='w')
L2 = Label(frame2, text="2、* 请输入要生成的文件类型（以逗号隔开）", font=('Arial 10 bold'))
L2.pack(side="top",ipadx=5)

frame3=Frame(myWindow)
frame3.grid(row=1, column=0, sticky='w')
L3 = Label(frame2, text="2、* 请输入要生成的文件类型（以逗号隔开）", font=('Arial 10 bold'))
L3.pack(side="left")




#生成button函数
# for i in range(10):
# button1 = Checkbutton(myWindow,text=".pdf",command=click_checkbox,variable=button_var1)
# button2 = Checkbutton(myWindow,text=".docx",command=click_checkbox,variable=button_var2)
# button3 = Checkbutton(myWindow,text=".doc",command=click_checkbox,variable=button_var3)
# button4 = Checkbutton(myWindow,text=".txt",command=click_checkbox,variable=button_var4)
# button5 = Checkbutton(myWindow,text=".img",command=click_checkbox,variable=button_var5)
# button6 = Checkbutton(myWindow,text=".png",command=click_checkbox,variable=button_var6)
#
# button1.grid(row=2,column=2)
# button2.grid(row=2,column=3)
# button3.grid(row=2,column=4)
# button4.grid(row=2,column=5)
# button5.grid(row=2,column=6)
# button6.grid(row=2,column=7)


L1 = Label(myWindow, text="请输入要生成的文件类型（以逗号隔开）", font=('Arial 10 bold'), width=20, height=10).grid(row=1,column=1)
file_type = Entry(myWindow, bd=5, width=30)
file_type.grid(row=1,column=2)
path=StringVar()
# def path_verify():
#     if path.get()=="E:/txt":
#         messagebox.showerror("路径错误")
L2 = Label(myWindow, text="请选择目标文件夹路径", font=('Arial 8 bold'), width=20, height=10).grid(row=2,column=0)
target = Entry(myWindow, textvariable = path,validate='focusout')
target.grid(row = 2, column = 2)


L2 = Label(myWindow, text="请输入需要生成的文件大小（MB）", font=('Arial 8 bold'), width=40, height=10).grid(row=4,column=1)
file_size = Entry(myWindow, bd=5, width=30)
file_size.grid(row=4,column=2)

L2 = Label(myWindow, text="请输入需要组合的文件名称字符(按逗号隔开)", font=('Arial 8 bold'), width=40, height=10).grid(row=7,column=1)
file_name = Entry(myWindow, bd=5, width=30)
file_name.grid(row=7,column=2)


def click_confirm():
    """
    按钮点击事件
    """
    # condict=dict()
    # condict["file_type"]=file_type.get()
    # condict["target_path"]=target.get()
    # condict["file_size"]=file_size.get()
    file_name_list=file_name.get().split(',')
    file_type_list=file_type.get().split(",")
    try:
        gen.generate_file(target.get().strip(),file_name_list,file_type_list,int(file_size.get()))
    except (FileNotFoundError, NotADirectoryError):
        messagebox.showerror("结果","文件生成失败，请选择有效的目录")
    else:
        messagebox.showinfo("结果", "文件生成成功")
def selectPath():
    path_=askdirectory()   #获取文件目录
    path.set(path_)
    #进入消息循环
b1 = Button(myWindow, text='确定', relief='raised', width=5, height=2,command=click_confirm).grid(row=8,column=1)
Button(myWindow, text = "请选择文件的生成位置", command = selectPath).grid(row = 2, column = 3)
if __name__ == '__main__':

    myWindow.mainloop()

