from posixpath import dirname
from PIL import Image
import os
dirNameDefault = r"Z:\001\img"

def renamFilesInDir(dirFiles):
    listFiles = [f for f in os.listdir(dirFiles) if os.path.isfile(os.path.join(dirFiles, f))]
    filesInfo = []
    for fileName in listFiles:
        imageName = os.path.join(dirFiles,fileName)
        #print(f"File: {fileName} FullName: {imageName}")
        try:
            image = Image.open(imageName)
        except Exception as er:
            print(er)
            continue
        width, height = image.size # extract width and height from output tuple
        # print(f"File: {imageName} Size:{width} X {height}")
        image.close()
        filesInfo.append({'file':imageName,'bname':fileName,'width':width,'height':height})
    if len(filesInfo)==0:
        return
    fileStaticWidth = [] # Статистика файлов по ширине ландшафт
    fileStaticHight = [] # Статистика файлов по высоте портрет
    dirNameWidth = "" # Имя каталога ландшафт
    dirNameHeight = "" # Имя каталога портрет
    for fileInfo in filesInfo:
        if fileInfo['width']>fileInfo['height']:
            fileStaticWidth.append(str(fileInfo['width'])+"x"+str(fileInfo['height']))
        else:
            fileStaticHight.append(str(fileInfo['width'])+"x"+str(fileInfo['height']))
    if len(fileStaticWidth)>0:
        dictStaticWidth = {i:fileStaticWidth.count(i) for i in fileStaticWidth}        
        #print(f"Width: {dictStaticWidth}")
        maxVal = 0
        for key, value in dictStaticWidth.items():
            #print(key, '->', value)        
            if value>maxVal:
                maxVal = value
                dirNameWidth = key
    else:
        dictStaticWidth = False
    if len(fileStaticHight)>0:    
        dictStaticHight = {i:fileStaticHight.count(i) for i in fileStaticHight}        
        #print(f"Height: {dictStaticHight}")
        maxVal = 0
        for key, value in dictStaticHight.items():
            #print(key, '->', value)        
            if value>maxVal:
                maxVal = value
                dirNameHeight = key
    else:
        dictStaticHight = False
        
    #print(f"Dir name width: {dirNameWidth}")    
    #print(f"Dir name height: {dirNameHeight}")    
    
    for fileInfo in filesInfo:
        if fileInfo['width']>fileInfo['height']:
            nameDir = dirNameWidth
        else:
            nameDir = dirNameHeight
        nameDir = os.path.join(dirFiles,nameDir)
        dirNameList = os.path.basename(nameDir).split('x')
        imageWidth,imageHeight = int(dirNameList[0]),int(dirNameList[1])
        isErrorFile = False # Есть ошибка в файле
        isDeleteFile = False # Удалять файл
        textComment = ''
        if fileInfo['width']<imageWidth:
            isErrorFile,textComment = (True,f"Small width {fileInfo['width']} x {fileInfo['height']} ")
        if fileInfo['height']<imageHeight:
            isErrorFile,textComment = (True,f"Small height {fileInfo['width']} x {fileInfo['height']} ")
        if isErrorFile:
            print(f"File name: {fileInfo['file']} {textComment}")    
            if fileInfo['width']<200:
                isDeleteFile = True
            if fileInfo['width']==525:
                isDeleteFile = True
            if fileInfo['height'] <= 1024 and fileInfo['width'] <= 700:
                isDeleteFile = True
        if isDeleteFile:
            print(f"{textComment} Delete file: {fileInfo['file']}")
            os.remove(fileInfo['file'])
        #if os.path.exists(nameDir)==False:
        #    os.makedirs(nameDir)
        #newfileName = os.path.join(nameDir,fileInfo['bname'])
        #
        #print(fileInfo)

def main(dirName):
    listDirs=[] # Список содержит имена каталогов
    for f in os.listdir(dirName):
        subdirName = os.path.join(dirName, f)
        if os.path.isdir(subdirName):
            listDirs.append(subdirName)

    #print(listDirs)
    for subdirName in listDirs:
        #print(f"Dir: {subdirName}")
        renamFilesInDir(subdirName)

if __name__ == '__main__':
    dirName = input(f"Enter dir name (defautl {dirNameDefault}):")
    if len(dirName)==0:
        dirName = dirNameDefault
    main(dirName)