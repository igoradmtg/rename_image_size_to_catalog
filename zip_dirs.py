import os
import zipfile
# Каталог исходных файлов по умолчанию
dirNameDefault = r"z:\001\img" # r"Y:\vid\img"
# Каталог новый
dirNameOut = r"w:\upl2_zip" # r"y:\upl1"        
# Добавлять файл ссылок
isAddFileLinks = True
# Имя файла который содержит ссылки
fileNameLinks = "links_telegram_chanel.txt"
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

def createZipFromDir(dirNameTmp,baseNameTmp):
    fileNameZip = os.path.join(dirNameOut,baseNameTmp + ".zip")
    with zipfile.ZipFile(fileNameZip, 'w', zipfile.ZIP_DEFLATED, True, 9) as zipf:
        zipdir(dirNameTmp, zipf)
        if isAddFileLinks==True:
            zipf.write(fileNameLinks,"_readme.txt")
    return fileNameZip    

def getDirList(dirName):
    listDirs=[] # Список содержит имена каталогов
    for f in os.listdir(dirName):
        subdirName = os.path.join(dirName, f)
        if os.path.isdir(subdirName):
            listDirs.append({'fullName':subdirName,'baseName':f})
    return listDirs

def deleteFilesInDir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            fullName = os.path.join(root, file)
            print(f"File: {fullName}")
            os.remove(fullName)

def main(dirName):
    listDirs = getDirList(dirName) # Список содержит имена каталогов
    #print(listDirs)
    for subdirName in listDirs:
        print(f"Dir: {subdirName['fullName']}")
        fileNameZip = createZipFromDir(subdirName['fullName'],subdirName['baseName'])
        if os.path.isfile(fileNameZip):
            deleteFilesInDir(subdirName['fullName'])
    
if __name__ == '__main__':
    dirName = input(f"Enter dir name (defautlt) {dirNameDefault}):")
    if len(dirName)==0:
        dirName = dirNameDefault
    main(dirName)