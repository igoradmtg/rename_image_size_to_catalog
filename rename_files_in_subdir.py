from posixpath import dirname
from PIL import Image
import os
dirNameDefault = r"Z:\LS\000"

def getDirList(dirName):
    listDirs=[] # Список содержит имена каталогов
    for f in os.listdir(dirName):
        subdirName = os.path.join(dirName, f)
        if os.path.isdir(subdirName):
            listDirs.append({'fullName':subdirName,'baseName':f})
    return listDirs

def getFileList(dirName):
    listDirs=[] # Список содержит имена каталогов
    for f in os.listdir(dirName):
        subdirName = os.path.join(dirName, f)
        if os.path.isfile(subdirName):
            listDirs.append({'fullName':subdirName,'baseName':f})
    return listDirs

def main(dirName):
    listDirs = getDirList(dirName) # Список содержит имена каталогов
    #print(listDirs)
    for subdirName in listDirs:
        #newDirName = 
        print(f"Dir: {subdirName['fullName']}")
        listFiles = getFileList(subdirName['fullName'])
        cntFiles = 0
        for fileName in listFiles:
            cntFiles += 1
            fileNameOld, fileExtension = os.path.splitext(fileName['baseName'])
            newName = str(cntFiles).zfill(4) + fileExtension
            newFullName = os.path.join(subdirName['fullName'],newName)
            if os.path.isfile(newFullName):
                continue
            print(f"Rename: {fileName['fullName']} New name: {newFullName}")    
            os.rename(fileName['fullName'],newFullName)
        #os.rename(subdirName['fullName'],newName)
        #renamFilesInDir(subdirName)

if __name__ == '__main__':
    dirName = input(f"Enter dir name (defautlt) {dirNameDefault}):")
    if len(dirName)==0:
        dirName = dirNameDefault
    main(dirName)