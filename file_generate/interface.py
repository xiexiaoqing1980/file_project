from tkinter import *
from tkinter.filedialog import askdirectory
import gennerate_file as gen
from tkinter import messagebox



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


L1 = Label(myWindow, text="请选择要生成的文件类型（可多选）", font=('Arial 8 bold'), width=20, height=1).grid(row=2,column=1)
button_var1=IntVar()
button_var2=IntVar()
button_var3=IntVar()
button_var4=IntVar()
button_var5=IntVar()
button_var6=IntVar()
file_type_list=[".pdf",".docx",".doc",".txt",".img"]
selected_type=[]
v=[]

for type in file_type_list:
    v.append(IntVar())
    Checkbutton(myWindow, text=type, variable=v[-1]).grid()

for each in v:#显示状态的框
　




def click_checkbox():
    if button_var1.get():
        file_type_list.insert(".pdf")



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


L1 = Label(myWindow, text="请输入要生成的文件类型（以逗号隔开）", font=('Arial 8 bold'), width=20, height=1).grid(row=1,column=1)
file_type = Entry(myWindow, bd=5, width=30)
file_type.grid(row=1,column=2)

path=StringVar()
L2 = Label(myWindow, text="请选择目标文件夹路径", font=('Arial 8 bold'), width=20, height=10).grid(row=3,column=1)
target = Entry(myWindow, textvariable = path)
target.grid(row = 3, column = 2)


L2 = Label(myWindow, text="请输入需要生成的文件大小（MB）", font=('Arial 8 bold'), width=20, height=10).grid(row=4,column=1)
file_size = Entry(myWindow, bd=5, width=30)
file_size.grid(row=4,column=2)

L2 = Label(myWindow, text="请输入文件名称", font=('Arial 8 bold'), width=20, height=10).grid(row=7,column=1)
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
    except:
        print("error")
    else:
        messagebox.showinfo("结果","文件生成成功")


def selectPath():
    path_=askdirectory()   #获取文件目录
    path.set(path_)



    #进入消息循环
b1 = Button(myWindow, text='确定', relief='raised', width=8, height=5,command=click_confirm).grid(row=4,column=4)
Button(myWindow, text = "请选择文件的生成位置", command = selectPath).grid(row = 3, column = 3)
if __name__ == '__main__':

    myWindow.mainloop()


