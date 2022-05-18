from PIL import Image
import os
dirName = "z:/files"

def renamFilesInDir(dirFiles):
    listFiles = [f for f in os.listdir(dirFiles) if os.path.isfile(os.path.join(dirFiles, f))]
    filesInfo = []
    for fileName in listFiles:
        imageName = os.path.join(dirFiles,fileName)
        #print(f"File: {fileName} FullName: {imageName}")
        image = Image.open(imageName)
        width, height = image.size # extract width and height from output tuple
        print(f"File: {imageName} Size:{width} X {height}")
        image.close()
        filesInfo.append({'file':imageName,'bname':fileName,'width':width,'height':height})
        
    for fileInfo in filesInfo:
        nameDir = str(fileInfo['width']) + 'x' + str(fileInfo['height'])
        nameDir = os.path.join(dirFiles,nameDir)
        if os.path.exists(nameDir)==False:
            os.makedirs(nameDir)
        newfileName = os.path.join(nameDir,fileInfo['bname'])
        os.rename(fileInfo['file'],newfileName)
        print(fileInfo)
        
listDirs=[] # Список содержит имена каталогов
for f in os.listdir(dirName):
    subdirName = os.path.join(dirName, f)
    if os.path.isdir(subdirName):
        listDirs.append(subdirName)
for subdirName in listDirs:
    renamFilesInDir(subdirName)
#print(listDirs)
