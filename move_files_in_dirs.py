from posixpath import dirname
from PIL import Image
import os
#dirNameDefault = r"w:\001\img2"
dirNameDefault = r"z:\001\img"
# Проходим по всем каталогам первого уровня
# Находим подкаталоги, переносим файлы в каталоги первого уровня
def renamFilesInDir(dirFiles,upDir):
    global cnt
    listFiles=[] # Список содержит имена каталогов
    for f in os.listdir(dirFiles):
        fullNameFile = os.path.join(dirFiles, f)
        if os.path.isfile(fullNameFile):
            listFiles.append(fullNameFile)
    # Номер файла
    print(f"Files {dirFiles}")
    print(listFiles)
    for fullNameFile in listFiles:
        fileNameOld, fileExtension = os.path.splitext(fullNameFile)
        newName = os.path.join(upDir,str(cnt).zfill(5)+fileExtension)
        print(f"File: {fileNameOld} {newName}")
        cnt += 1 
        os.rename(fullNameFile,newName)
        #if os.rename()

def main(dirName):
    global cnt
    listDirs=[] # Список содержит имена каталогов
    for f in os.listdir(dirName):
        subdirName = os.path.join(dirName, f)
        if os.path.isdir(subdirName):
            listDirs.append(subdirName)

    print(listDirs)
    for subdirName in listDirs:
        listDirs2=[] # Список содержит имена каталогов
        for f in os.listdir(subdirName):
            subdirName2 = os.path.join(subdirName, f)
            if os.path.isdir(subdirName2):
                listDirs2.append(subdirName2)
        print(f"Dir name: {subdirName}")
        print(listDirs2)
        cnt = 1
        for subdirName2 in listDirs2:
            renamFilesInDir(subdirName2,subdirName)

if __name__ == '__main__':
    dirName = input(f"Enter dir name (defautl {dirNameDefault}):")
    if len(dirName)==0:
        dirName = dirNameDefault
    main(dirName)