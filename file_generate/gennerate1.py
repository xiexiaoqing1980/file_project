
import os
import shutil


def generate_file(target,fileNameList,fileTypeList):
    """生成文件"""
    if not os.path.exists(target) or os.path.isfile(target):
        print("error target")
    else :
        path = os.path.join(target,'/file_folder')
        if not os.path.exists(path):  #如果文件夹不存在就生成新的文件夹
            os.mkdir(path)    #生成文件夹
        else:
            shutil.rmtree(path)
            os.mkdir(path)
        for fileType in fileTypeList:
            for filename in fileNameList:
                fullpath=os.path.join(path,filename+fileType)
                with open(fullpath,'w') as fp:
                    fp.write("The file is generated automatically")


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
    """复制文件并重命名文件"""
    if  not os.path.exists(src_file_path):
        raise FileNotFoundError
    if os.path.isfile(src_file_path):
        raise NotADirectoryError
    src_file_list= os.listdir(src_file_path)    #获取资源下的所有文件和文件夹
    suffix_list=[]
    fileNameList = generate_filenamelist(char_list)
    for src_file in src_file_list:
        suffix = src_file[src_file.index("."):]  #获取后缀
        # suffix_list.append(suffix)   #获取后缀名列表
        for fileName in fileNameList:
            shutil.copy(os.path.join(src_file_path,src_file),os.path.join(target_file,fileName+suffix))




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
    fileTypeList=[".docx",".gif",".pdf",".doc"]
    charlist=["&","%","test"]
    # fileNameList=generate_filenamelist(charlist)
    # generate_file("D:/",fileNameList,fileTypeList)
    path="D:/src_file"
    target="E:/File_folder"
    copy_And_rename_File(path,target,charlist)

     # deleteAllFiles("D:/file_folder")



