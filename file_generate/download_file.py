from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import  os
import shutil

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

L1 = Label(frame1, text="*1、请选择要下载的文件类型（可多选）", font=('GB2312 10 bold'),padx = 0)
L1.pack(side="left")

file_type_list1=[".pdf",".docx",".doc",".txt","tiff",".png",".jpg",".gif",".jsp",".xls",".xlsx"]
file_type_list2=[".jpeg",".pptx",".ppt",".mp4",".bmp",".dcx",".dib",".exe",".html",".jar",".war"]

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

L2 = Label(frame4, text=" 自定义的下载文件类型（以逗号隔开）", font=('GB2312 10 bold'))
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
L4 = Label(frame6, text="下载的相同文件数，默认生成1份", font=('GB2312 10 bold'),height=3)
L4.pack(side="left")
file_amount = Entry(frame6, width=10)
file_amount.pack(side="left")

L5 = Label(frame7, text="若需要重命名，请输入文件名(不能包含以下特殊字符： \/:*?<>|"+'"'+")", font=('GB2312 10 bold'),height=3)
L5.pack(side="top")
file_name = Entry(frame7,  width=30)
file_name.pack(side="left")

# def generate_filenamelist(charlist):
#     """生成文件名的函数，此处用到递归"""
#     if len(charlist)<=1:    #如果长度为1，说明只有一个字符/字符串，排列组合就是它自己
#         return charlist
#     filenameList=[]  #保存字符串的所有可能排列组合
#     for i in range(len(charlist)): #确定列表中的的第一个字母是谁，有n种可能（n为charList的长度)
#         for j in generate_filenamelist(charlist[0:i]+charlist[i+1:]):
#             filenameList.append(charlist[i]+j)
#
#     return filenameList

# def generate_file(target,charlist,fileTypeList,fileSize):
#     """生成文件
#     :param target 生成目录
#     :param fileNameList 文件名列表
#     :param fileTypeList 文件后缀名
#     :param fileSize  文件大小
#     """
#     if not os.path.exists(target):
#         raise FileNotFoundError
#     if  not os.path.isdir(target):
#         raise NotADirectoryError
#     fileNameList=generate_filenamelist(charlist)
#     # data_size = 0
#     for fileType in fileTypeList:
#         count = 0
#         for filename in fileNameList:
#             fullpath=os.path.join(target,filename+fileType.strip())
#             with open(fullpath,'wb') as fp:
#                 # fp.seek(fileSize)
#                 # fp.write(b'\x00')    #写入空白字符
#                 bytes=os.urandom(fileSize*1024*1024)     #以MB为单位
#                 fp.write(bytes)   #随即产生n个字节的字符串，可以作为随机加密key使用~
#                 # count=count+1

def copy_And_rename_File(wanted_type ,target_file,fileName,file_amount):
    """复制文件并重命名文件
    :param src_file_path
    :param target_file
    :param char_list
    """
    # path=init_files(src_file_path,target_file)
    src_file_list= os.listdir("../resource")    #获取资源下的所有文件和文件夹
    suffix_list=[]
    amount=1
    if file_amount:
        amount=int(file_amount)

    for type in wanted_type:
        flag=False
        for src_file in src_file_list:
            # if type in src_file:
            if src_file.rfind(type)!=-1:
                # suffix = src_file[src_file.rfind("."):]  #获取后缀
                flag=True
                name=src_file[0:src_file.rfind(".")]
                if fileName :      #如果文件名不为空,则替换名称
                    # suffix_list.append(suffix)   #获取后缀名列表
                    name=fileName
                if amount>1:
                    for i in range(0,amount):
                        shutil.copy(os.path.join("../resource",src_file),os.path.join(target_file,name+str(i)+type))
                else:
                    shutil.copy(os.path.join("../resource", src_file), os.path.join(target_file, name + type))
        if not flag:
            messagebox.showinfo("结果","未找到{}的文件类型".format(type))

        # messagebox.showwarning("")

def init_files(*file_path) :
    for path_ in file_path:           #主动抛出异常
        if  not os.path.exists(path_):
            raise FileNotFoundError
        if  os.path.isfile(path_):
            raise NotADirectoryError
    # path = os.path.join(file_path[-1], 'file_folder')

    # if not os.path.exists(path):  # 如果目标文件夹不存在就生成新的文件夹
    #     os.mkdir(path)  # 生成目标文件夹，会把原来
    # else:
    #     shutil.rmtree(path)  # 把生成的文件删除
    #     os.mkdir(path)       #此处可能出现异常       #不进行覆盖操作
    return file_path[-1]

def click_download():
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


    # if not file_name.get().strip():
    #     messagebox.showwarning("结果", "请输入文件名字符")
    #     return

    # forbidden_chars="\/:*?<>|"+'"'
    # for char in forbidden_chars:
    #     if char in file_name.get().strip():
    #         messagebox.showwarning("结果", "请输入有效名称字符")
    #         return

    file_name_list = file_name.get().split(',')
    try:
        copy_And_rename_File(total_file_type,target.get().strip(),file_name.get(),file_amount.get())
    except (FileNotFoundError, NotADirectoryError):
        messagebox.showwarning("结果","文件生成失败，请选择有效的目录")
    else:
        messagebox.showinfo("结果", "文件生成成功")

def copy_dir(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            path_abs=os.path.join(path,file)
            if os.path.isfile(path_abs):
                shutil.copy(path_abs,os.path.join("../resource",file))
            else:
                copy_dir(path_abs)
    else:
        shutil.copy(path ,os.path.join("../resource",path))


def click_upload():

    path=target.get()
    if not os.path.exists(path):
        messagebox.showwarning("结果", "请选择有效的目录或者文件")
        return
    if os.path.isdir(path):    #上传目录
        copy_dir(path)
    elif os.path.isfile(path):
        shutil.copy(path,os.path.join("../resource",path))









b1 = Button(frame9, text='下载附件', relief='raised', width=10, height=2,command=click_download,font=('GB2312 10 bold'))
b1.pack(side="left",padx=20)

b2 = Button(frame9, text='上传附件', relief='raised', width=10, height=2,command=click_download,font=('GB2312 10 bold'))
b2.pack(side="left",padx=5)


if __name__ == '__main__':

    # myWindow.mainloop()
    click_upload()



