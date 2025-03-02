import os
import shutil
import secrets
# Копируем файлы в случайном порядке в подкаталоги по несколько файлов
dirNameDefault = r"w:\LS\LS\Cinderella_Girl" # Каталог по умолчанию
dirNameOut = r"w:\001\img" # Каталог для по умолчанию
dirNameStart = "Cinderella_Girl_rnd_"
numFilesInDir = 300 # Количество файлов в каталоге
curDir = 1 # Нумерация каталогов
curFile = 1 # Нумерация файлов
secretsGenerator = secrets.SystemRandom()
filesJpg = [os.path.join(dp, f) for dp, dn, filenames in os.walk(dirNameDefault) for f in filenames if os.path.splitext(f)[1] == '.jpg']
filesRand = secretsGenerator.sample(filesJpg, len(filesJpg))
for inputFile in filesRand:
    newDirName = os.path.join(dirNameOut,dirNameStart+str(curDir).zfill(4));
    if os.path.isdir(newDirName)==False:
        print(f"Make dir: {newDirName}")
        os.mkdir(newDirName)
    newFileName = os.path.join(newDirName,str(curFile).zfill(8)+".jpg")
    #print(f" {inputFile},{newFileName}")
    shutil.copyfile(inputFile,newFileName)
    curFile += 1
    if curFile>numFilesInDir:
        curFile = 1
        curDir += 1 