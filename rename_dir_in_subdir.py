from posixpath import dirname
from PIL import Image
import os
dirNameDefault = r"Z:\LS\Collection"

def getDirList(dirName):
    listDirs=[] # Список содержит имена каталогов
    for f in os.listdir(dirName):
        subdirName = os.path.join(dirName, f)
        if os.path.isdir(subdirName):
            listDirs.append({'fullName':subdirName,'baseName':f})
    return listDirs

def main(dirName):
    listDirs = getDirList(dirName) # Список содержит имена каталогов
    #print(listDirs)
    for subdirName in listDirs:
        #newDirName = 
        print(f"Dir: {subdirName['fullName']}")
        listDirs2 = getDirList(subdirName['fullName'])
        for subdirName2 in listDirs2:
            newName = subdirName['fullName'] + " " + subdirName2['baseName']
            print(f"Dir: {subdirName2['fullName']} New name: {newName}")
            os.rename(subdirName2['fullName'],newName)
        #renamFilesInDir(subdirName)

if __name__ == '__main__':
    dirName = input(f"Enter dir name (defautlt) {dirNameDefault}):")
    if len(dirName)==0:
        dirName = dirNameDefault
    main(dirName)