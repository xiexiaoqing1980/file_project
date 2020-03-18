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
frame1.grid(row=0,column=0, sticky='w',ipady=5)

frame2=Frame(myWindow)
frame2.grid(row=1,column=0, sticky='w',ipady=5)


frame3=Frame(myWindow)
frame3.grid(row=2,column=0, sticky='w',ipady=5)

frame4=Frame(myWindow)
frame4.grid(row=3,column=0, sticky='w',ipady=5)

frame5=Frame(myWindow)
frame5.grid(row=4,column=0, sticky='w',ipady=5)

frame6=Frame(myWindow)
frame6.grid(row=5,column=0, sticky='w',ipady=5)

frame7=Frame(myWindow)
frame7.grid(row=6,column=0, sticky='w',ipady=5)


L1 = Label(frame1, text="*1、请选择要生成的文件类型（可多选）", font=('Arial 10 bold'),padx = 0)
L1.pack(side="left")

file_type_list1=[".pdf",".docx",".doc",".txt",".img",".png",".jpg",".gif",".jpeg",".xls",".xlsx"]
file_type_list2=[".jpeg","pptx","ppt",".jfif",".bmp",".dcx",".dib",".exe",".html",".jar",".war"]

selected_type=[]
v=[]          #状态数组

def click_checkbox():
    global selected_type        #声明为全局变量，可以在局部变量中修改值
    each_select=[]
    for state in v:
        if state.get() !="":
            each_select.append(state.get())
    selected_type = each_select



for i in range(len(file_type_list1)):
    v.append(StringVar())
    Checkbutton(frame2, text=file_type_list1[i], variable=v[-1],command=click_checkbox,onvalue=file_type_list1[i],offvalue="").pack(side="left")

for i in range(len(file_type_list2)):
    v.append(StringVar())
    Checkbutton(frame3, text=file_type_list2[i], variable=v[-1],command=click_checkbox,onvalue=file_type_list2[i],offvalue="").pack(side="left")




# frame2=Frame(myWindow)
# frame2.grid(row=1, column=0, sticky='w',ipady=1)
L2 = Label(frame4, text=" 自定义的文件类型（以逗号隔开）", font=('Arial 10 bold'))
L2.pack(side="left")
file_type = Entry(frame4, width=50)
file_type.pack(side="left")

path=StringVar()
L3=Label(frame5, text="*2、请选择目标文件夹路径", font=('Arial 10 bold'), height=3)
L3.pack(side="left")
target = Entry(frame5, textvariable = path,validate='focusout')
target.pack(side="left")

def selectPath():
    path_=askdirectory()   #获取文件目录
    path.set(path_)

Button(frame5, text = "请选择文件的生成位置", command = selectPath).pack(side="left")



L4 = Label(frame6, text="*3、请输入需要生成的文件大小（MB）", font=('Arial 10 bold'),height=3)
L4.pack(side="left")
file_size = Entry(frame6, bd=5, width=30)
file_size.pack(side="left")

L5 = Label(frame7, text="*4、请输入需要组合的文件名称字符，按逗号隔开", font=('Arial 10 bold'),height=3)
L5.pack(side="left")
file_name = Entry(frame7, bd=5, width=30)
file_name.pack(side="left")


if __name__ == '__main__':

    myWindow.mainloop()


