
import os
import shutil


def generate_file(target,filename,fileTypeList):
    """生成文件"""
    if not os.path.exists(target) or os.path.isfile(target):
        print("error target")
    else :
        path = os.path.join(target,'/file_folder')
        if not os.path.exists(path):  #如果文件夹不存在就生成新的文件夹
            os.mkdir(path)    #生成文件夹
        # else:
        #     shutil.rmtree(path)
        #     os.mkdir(path)
        for fileType in fileTypeList:
            fullpath=os.path.join(path,filename+fileType)
            with open(fullpath,'w') as fp:
                fp.write("The file is generated automatically")

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
    filenamelist=[" ","&","%","test"]
    generate_file("D:/",filenamelist,fileTypeList)
     # deleteAllFiles("D:/file_folder")


