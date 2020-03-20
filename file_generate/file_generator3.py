from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import  os

#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('File Generator')
#设置窗口大小
width = 600
height = 450
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

frame8=Frame(myWindow)
frame8.grid(row=7,column=0,ipady=5,sticky='w')

frame9=Frame(myWindow)
frame9.grid(row=8,column=0,ipady=5)

L1 = Label(frame1, text="*1、请选择要生成的文件类型（可多选）", font=('GB2312 10 bold'),padx = 0)
L1.pack(side="left")

file_type_list1=[".pdf",".docx",".doc",".txt",".img",".png",".jpg",".gif",".jpeg",".xls",".xlsx"]
file_type_list2=[".jpeg",".pptx",".ppt",".jfif",".bmp",".dcx",".dib",".exe",".html",".jar",".war"]

selected_type=set()
v1=[]
v2=[]
#状态数组

def click_checkbox():
    global selected_type        #声明为全局变量，可以在局部变量中修改值
    each_select=set()
    for state1 in v1:
        if state1.get() !="":
            each_select.add(state1.get())

    for state2 in v2:
        if state2.get() !="":
            each_select.add(state2.get())

    selected_type = each_select

for i in range(len(file_type_list1)):
    v1.append(StringVar())
    Checkbutton(frame2, text=file_type_list1[i], variable=v1[-1],command=click_checkbox,onvalue=file_type_list1[i],offvalue="").pack(side="left")

for i in range(len(file_type_list2)):
    v2.append(StringVar())
    Checkbutton(frame3, text=file_type_list2[i], variable=v2[-1],command=click_checkbox,onvalue=file_type_list2[i],offvalue="").pack(side="left")

L2 = Label(frame4, text=" 自定义的文件类型（以逗号隔开）", font=('GB2312 10 bold'))
L2.pack(side="left")
file_type = Entry(frame4, width=50)
file_type.pack(side="left")

path=StringVar()
L3=Label(frame5, text="*2、请选择目标文件夹路径", font=('GB2312 10 bold'), height=3)
L3.pack(side="left",ipadx=5)

def selectPath():
    path_=askdirectory()   #获取文件目录
    path.set(path_)
Button(frame5, text = "请选择文件的生成位置", font=('GB2312 10 bold'),command = selectPath).pack(side="left")

target = Entry(frame5, textvariable = path,validate='focusout',width=40)
target.pack(side="left")
L4 = Label(frame6, text="*3、请输入文件大小（MB）", font=('GB2312 10 bold'),height=3)
L4.pack(side="left")
file_size = Entry(frame6, width=30)
file_size.pack(side="left")

L5 = Label(frame7, text="*4、请输入需要组合的文件名称字符，按逗号隔开(不能包含以下特殊字符： \/:*?<>|"+'"'+")", font=('GB2312 10 bold'),height=3)
L5.pack(side="top")
file_name = Entry(frame7,  width=30)
file_name.pack(side="left")

def generate_filenamelist(charlist):
    """生成文件名的函数，此处用到递归"""
    if len(charlist)<=1:    #如果长度为1，说明只有一个字符/字符串，排列组合就是它自己
        return charlist
    filenameList=[]  #保存字符串的所有可能排列组合
    for i in range(len(charlist)): #确定列表中的的第一个字母是谁，有n种可能（n为charList的长度)
        for j in generate_filenamelist(charlist[0:i]+charlist[i+1:]):
            filenameList.append(charlist[i]+j)

    return filenameList

def generate_file(target,charlist,fileTypeList,fileSize):
    """生成文件
    :param target 生成目录
    :param fileNameList 文件名列表
    :param fileTypeList 文件后缀名
    :param fileSize  文件大小
    """
    if not os.path.exists(target):
        raise FileNotFoundError
    if  not os.path.isdir(target):
        raise NotADirectoryError
    fileNameList=generate_filenamelist(charlist)
    # data_size = 0
    for fileType in fileTypeList:
        count = 0
        for filename in fileNameList:
            fullpath=os.path.join(target,filename+fileType.strip())
            with open(fullpath,'wb') as fp:
                # fp.seek(fileSize)
                # fp.write(b'\x00')    #写入空白字符
                bytes=os.urandom(fileSize*1024*1024)     #以MB为单位
                fp.write(bytes)   #随即产生n个字节的字符串，可以作为随机加密key使用~
                # count=count+1

def click_confirm():
    """
    按钮点击事件
    """
    total_file_type=set()  #每次点击确定，重新加载添加的数据

    file_type_list = file_type.get().strip().split(",")

    for type1 in selected_type:
        total_file_type.add(type1)
    for type2 in file_type_list:
        if type2:
            total_file_type.add(type2)

    if not total_file_type:
        messagebox.showwarning("结果", "请选择或者输入文件类型")
        return

    if not os.path.exists(target.get()) or not os.path.isdir(target.get()):
        messagebox.showwarning("结果", "请选择有效的目录")
        return
    if not file_size.get():
        messagebox.showwarning("结果", "请输入文件大小")
        return

    if not file_name.get().strip():
        messagebox.showwarning("结果", "请输入文件名字符")
        return

    forbidden_chars="\/:*?<>|"+'"'
    for char in forbidden_chars:
        if char in file_name.get().strip():
            messagebox.showwarning("结果", "请输入有效名称字符")
            return

    file_name_list = file_name.get().split(',')


    try:
        generate_file(target.get().strip(),file_name_list,total_file_type,int(file_size.get()))
    except (FileNotFoundError, NotADirectoryError):
        messagebox.showwarning("结果","文件生成失败，请选择有效的目录")
    else:
        messagebox.showinfo("结果", "文件生成成功")
b1 = Button(frame9, text='确定', relief='raised', width=5, height=2,command=click_confirm,font=('GB2312 10 bold'))
b1.pack(side="top")

if __name__ == '__main__':

    myWindow.mainloop()


