
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
    """生成文件的函数，此处用到递归"""
    if len(charlist)<=1:    #如果长度为1，说明只有一个字符/字符串，排列组合就是它自己
        return charlist
    filenameList=[]  #保存字符串的所有可能排列组合
    for i in range(len(charlist)): #确定列表中的的第一个字母是谁，有n种可能（n为charList的长度)
        for j in generate_filenamelist(charlist[0:i]+charlist[i+1:]):
            filenameList.append(charlist[i]+j)

    return filenameList



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
    charlist=[" ","&","%","test","#"]
    fileNameList=generate_filenamelist(charlist)
    generate_file("D:/",fileNameList,fileTypeList)

     # deleteAllFiles("D:/file_folder")



