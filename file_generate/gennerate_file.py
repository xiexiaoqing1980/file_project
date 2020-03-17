
import os
import shutil


# def generate_file(target,charlist,fileTypeList,fileSize,limit_count):
#     """生成文件
#     :param target 生成目录
#     :param fileNameList 文件名列表
#     :param fileTypeList 文件后缀名
#     :param fileSize  文件大小
#     """
#     path=init_files(target)
#     fileNameList=generate_filenamelist(charlist)
#
#     # data_size = 0
#     for fileType in fileTypeList:
#         count = 0
#         for filename in fileNameList:
#             if count<limit_count:
#                 fullpath=os.path.join(path,filename+fileType)
#                 with open(fullpath,'wb') as fp:
#                     # fp.seek(fileSize)
#                     # fp.write(b'\x00')    #写入空白字符
#                     bytes=os.urandom(fileSize*1024*1024)     #以MB为单位
#                     fp.write(bytes)   #随即产生n个字节的字符串，可以作为随机加密key使用~
#                 count=count+1
#             else:
#                 break
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
            fullpath=os.path.join(path,filename+"."+fileType.strip())
            with open(fullpath,'wb') as fp:
                # fp.seek(fileSize)
                # fp.write(b'\x00')    #写入空白字符
                bytes=os.urandom(fileSize*1024*1024)     #以MB为单位
                fp.write(bytes)   #随即产生n个字节的字符串，可以作为随机加密key使用~
                # count=count+1


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
        if src_file.rfind(".")!=-1:
            suffix = src_file[src_file.rfind("."):]  #获取后缀
            # suffix_list.append(suffix)   #获取后缀名列表
            for fileName in fileNameList:
                shutil.copy(os.path.join(src_file_path,src_file),os.path.join(path,fileName+suffix))

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





if __name__ == '__main__':
    fileTypeList=['exe', 'war', 'jar', 'sh', 'bat', 'py', 'php', 'jsp', 'asp', 'cmd', 'js', 'cgi', 'class', 'jspx', 'aspx', 'htm', 'html', 'htt', 'htx', 'mhtm', 'mhtml', 'shtm', 'shtml', 'acgi']
    charlist=["& $ @ #()_"]

    generate_file("G:/",charlist,fileTypeList,fileSize=2)
    path="G:/file_folder"
    target="E:/"
    # copy_And_rename_File(path,target,charlist)

     # deleteAllFiles("D:/file_folder")



