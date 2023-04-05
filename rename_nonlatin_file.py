from transliterate import translit
import os

def renamFilesInDir(dirFiles):
    return True

def main(dirName):
    listDirs=[] # Список содержит имена каталогов
    for f in os.listdir(dirName):
        subdirName = os.path.join(dirName, f)
        subdirName2 = os.path.join(dirName, str(translit(f, "ru",reversed = True)).replace("'",''))
        if os.path.isfile(subdirName):
            listDirs.append({'file1':subdirName,'file2':subdirName2})

    #print(listDirs)
    for infoName in listDirs:
        print(f"Dir: {infoName}")
        os.rename(infoName['file1'],infoName['file2'])
        ##renamFilesInDir(subdirName)

if __name__ == '__main__':
    dirNameDefault = r"/mnt/dsk3/zip"
    dirName = input(f"Enter dir name (defautl {dirNameDefault}):")
    if len(dirName)==0:
        dirName = dirNameDefault
    main(dirName)