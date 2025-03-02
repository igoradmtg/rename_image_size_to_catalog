from posixpath import dirname
from PIL import Image
import os
dirNameDefault = r"W:\001\img2"
dirNameOut = r"W:\001\img4"
maxFileSize = 1500*1024*1024;
def getDirList(dirName):
    listDirs=[] # Список содержит имена каталогов
    for f in os.listdir(dirName):
        subdirName = os.path.join(dirName, f)
        if os.path.isdir(subdirName):
            listDirs.append({'fullName':subdirName,'baseName':f})
    return listDirs

def getFilesList(dirName):
    listFiles=[] # Список содержит имена каталогов
    for f in os.listdir(dirName):
        fileName = os.path.join(dirName, f)
        if os.path.isfile(fileName):
            listFiles.append({'fullName':fileName,'baseName':f})
    return listFiles

def main(dirName):
    listDirs = getDirList(dirName) # Список содержит имена каталогов
    #print(listDirs)
    countFile = 1
    for subdirName in listDirs:
        #newDirName = 
        print(f"Dir: {subdirName['fullName']}")
        listFiles = getFilesList(subdirName['fullName'])
        fileSizeSum = 0
        dirCount = 1
        newDirName = os.path.join(dirNameOut,subdirName['baseName']+"_"+str(dirCount).zfill(3))
        os.mkdir(newDirName)
        for fileName in listFiles:
            fileSize = os.path.getsize(fileName['fullName'])
            if fileSizeSum+fileSize > maxFileSize:
                dirCount += 1
                newDirName = os.path.join(dirNameOut,subdirName['baseName']+"_"+str(dirCount).zfill(3))
                os.mkdir(newDirName)
                fileSizeSum = 0
                countFile = 1
            fileSizeSum +=fileSize
            #newFileName = os.path.join(newDirName,fileName['baseName'])
            newFileName = os.path.join(newDirName,str(countFile).zfill(5)+".jpg")
            countFile += 1
            os.rename(fileName['fullName'],newFileName)
            print(f"  File: {fileName['fullName']} NewName: {newFileName} Size: {fileSize} SummSize: {fileSizeSum}")

if __name__ == '__main__':
    dirName = input(f"Enter dir name (defautlt) {dirNameDefault}):")
    if len(dirName)==0:
        dirName = dirNameDefault
    main(dirName)