
import os
import shutil
import random


def generate_file(target,fileNameList,fileTypeList,fileSize):
    """生成文件"""
    path=init_files(target)
    # data_size = 0
    for fileType in fileTypeList:
        for filename in fileNameList:
            fullpath=os.path.join(path,filename+fileType)
            with open(fullpath,'a+') as fp:
                # while data_size < fileSize:
                #     fp.write('1')  # 写入数字
                #     data_size = os.path.getsize(fullpath)
                fp.seek(1024*1024*1024*fileSize)  #以MB为单位
                fp.write('1')



def generate_filenamelist(charlist):
    """生成文件名的函数，此处用到递归"""
    if len(charlist)<=1:    #如果长度为1，说明只有一个字符/字符串，排列组合就是它自己
        return charlist
    filenameList=[]  #保存字符串的所有可能排列组合
    for i in range(len(charlist)): #确定列表中的的第一个字母是谁，有n种可能（n为charList的长度)
        for j in generate_filenamelist(charlist[0:i]+charlist[i+1:]):
            filenameList.append(charlist[i]+j)

    return filenameList

def copy_And_rename_File( src_file_path,target_file,char_list):
    """复制文件并重命名文件
    :param src_file_path
    :param target_file
    :param char_list
    """
    path=init_files(src_file_path,target_file)
    src_file_list= os.listdir(src_file_path)    #获取资源下的所有文件和文件夹
    suffix_list=[]
    fileNameList = generate_filenamelist(char_list)
    for src_file in src_file_list:
        suffix = src_file[src_file.index("."):]  #获取后缀
        # suffix_list.append(suffix)   #获取后缀名列表
        for fileName in fileNameList:
            shutil.copy(os.path.join(src_file_path,src_file),os.path.join(path,fileName+suffix))

def init_files(*file_path):
    for path in file_path:
        if  not os.path.exists(path):
            raise FileNotFoundError
        if os.path.isfile(path):
            raise NotADirectoryError
    path = os.path.join(file_path[-1], '/file_folder')
    if not os.path.exists(path):  # 如果目标文件夹不存在就生成新的文件夹
        os.mkdir(path)  # 生成目标文件夹
    else:
        shutil.rmtree(path)  # 把生成的文件删除
        os.mkdir(path)       #此处可能出现异常
    return path














# def deleteAllFiles(filePath):
#     if os.path.exists(filePath):
#         for dirpath ,dirnames,filenames in os.walk(filePath):
#             for name in filenames:
#                 os.remove(os.path.join(dirpath,name))   #递归删除文件
#         for folder in os.listdir(filePath):
#             name=os.path.join(filePath,folder)
#             if not os.listdir():
#                 os.rmdir(os.path.join(name))
        # os.rmdir()


if __name__ == '__main__':
    fileTypeList=[".doc"]
    charlist=["test"]
    fileNameList=generate_filenamelist(charlist)
    generate_file("D:/",fileNameList,fileTypeList,fileSize=1024*20)
    path="D:/src_file"
    target="E:/"
    # copy_And_rename_File(path,target,charlist)

     # deleteAllFiles("D:/file_folder")



