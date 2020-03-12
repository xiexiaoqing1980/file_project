import  os

def deleteAllFiles(filePath):
    if os.path.exists(filePath):
        for dirpath ,dirnames,filenames in os.walk(filePath):
            for name in dirnames:
                print(os.path.join(dirpath,name))
            for name in filenames:
                print(os.path.join(dirpath,name))

def get_size(fullpath,fileSize):
    data_size=0
    with open(fullpath, 'a+') as fp:
        while data_size < fileSize:
            fp.write('1')  # 写入数字
            data_size = os.path.getsize(fullpath)



if __name__ == '__main__':
    # deleteAllFiles("C:/Users/Administrator/Desktop/JSONView-for-Chrome-master")
    # dirs=os.listdir("D:/file_folder")
    # deleteAllFiles("D:/file_folder")
    # for file in dirs:
    # deleteAllFiles("D:/empty")
    #     print(file)
    get_size("D:/file_folder/test.doc",1024)
