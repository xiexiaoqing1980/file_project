import  os

def deleteAllFiles(filePath):
    if os.path.exists(filePath):
        for dirpath ,dirnames,filenames in os.walk(filePath):
            for name in dirnames:
                print(os.path.join(dirpath,name))
            for name in filenames:
                print(os.path.join(dirpath,name))





if __name__ == '__main__':
    # deleteAllFiles("C:/Users/Administrator/Desktop/JSONView-for-Chrome-master")
    # dirs=os.listdir("D:/file_folder")
    # deleteAllFiles("D:/file_folder")
    # for file in dirs:
    deleteAllFiles("D:/empty")
    #     print(file)