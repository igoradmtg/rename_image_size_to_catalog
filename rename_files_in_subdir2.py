# Импорт необходимых модулей
from posixpath import dirname  # Модуль для работы с путями в POSIX-совместимых системах
from PIL import Image  # Модуль для работы с изображениями (хотя в коде он не используется)
import os  # Модуль для работы с операционной системой (файлы, каталоги и т.д.)

# Путь к директории по умолчанию
dirNameDefault = r"Z:\001\img"
# Альтернативный путь к директории (закомментирован)
# dirNameDefault = r"w:\LS\_Save7zip"

# Функция для получения списка подкаталогов в указанной директории
def getDirList(dirName):
    listDirs = []  # Инициализация списка для хранения информации о каталогах
    for f in os.listdir(dirName):  # Перебор всех элементов в указанной директории
        subdirName = os.path.join(dirName, f)  # Формирование полного пути к элементу
        if os.path.isdir(subdirName):  # Проверка, является ли элемент каталогом
            # Добавление информации о каталоге в список
            listDirs.append({'fullName': subdirName, 'baseName': f})
    return listDirs  # Возврат списка каталогов

# Функция для получения списка файлов в указанной директории
def getFileList(dirName):
    listDirs = []  # Инициализация списка для хранения информации о файлах
    for f in os.listdir(dirName):  # Перебор всех элементов в указанной директории
        subdirName = os.path.join(dirName, f)  # Формирование полного пути к элементу
        if os.path.isfile(subdirName):  # Проверка, является ли элемент файлом
            # Добавление информации о файле в список
            listDirs.append({'fullName': subdirName, 'baseName': f})
    return listDirs  # Возврат списка файлов

# Функция для удаления пустых каталогов
def removeEmptyDirs(dirName):
    listDirs = getDirList(dirName)  # Получение списка подкаталогов
    for subdir in listDirs:  # Перебор всех подкаталогов
        removeEmptyDirs(subdir['fullName'])  # Рекурсивный вызов для удаления пустых подкаталогов
    if not os.listdir(dirName):  # Проверка, пуст ли каталог
        os.rmdir(dirName)  # Удаление пустого каталога
        print(f"Удален пустой каталог: {dirName}")

# Основная функция, которая выполняет переименование файлов
def main(dirName):
    listDirs = getDirList(dirName)  # Получение списка каталогов в указанной директории
    # print(listDirs)  # Отладочный вывод списка каталогов (закомментирован)
    
    for subdirName in listDirs:  # Перебор всех каталогов
        print(f"Dir: {subdirName['fullName']}")  # Вывод полного пути к текущему каталогу
        listDirs2 = getDirList(subdirName['fullName'])  # Получение списка подкаталогов в текущем каталоге
        
        if len(listDirs2) == 0:  # Если подкаталогов нет, переходим к следующему каталогу
            continue
        
        cntFiles = 0  # Счетчик файлов для формирования нового имени
        for subdirName2 in listDirs2:  # Перебор всех подкаталогов
            listFiles = getFileList(subdirName2['fullName'])  # Получение списка файлов в текущем подкаталоге
            for fileName in listFiles:  # Перебор всех файлов в подкаталоге
                cntFiles += 1  # Увеличение счетчика файлов
                fileNameOld, fileExtension = os.path.splitext(fileName['baseName'])  # Разделение имени файла и расширения
                newName = str(cntFiles).zfill(4) + fileExtension  # Формирование нового имени файла (с ведущими нулями)
                newFullName = os.path.join(subdirName['fullName'], newName)  # Формирование полного пути к новому имени файла
                
                if os.path.isfile(newFullName):  # Проверка, существует ли файл с таким именем
                    continue  # Если существует, пропускаем переименование
                
                # Вывод информации о переименовании
                print(f"Rename: {fileName['fullName']} New name: {newFullName}")
                os.rename(fileName['fullName'], newFullName)  # Переименование файла
    
    # Удаление пустых каталогов после завершения переименования
    removeEmptyDirs(dirName)

# Точка входа в программу
if __name__ == '__main__':
    # Запрос у пользователя пути к директории
    dirName = input(f"Enter dir name (default) {dirNameDefault}):")
    if len(dirName) == 0:  # Если пользователь не ввел путь, используется путь по умолчанию
        dirName = dirNameDefault
    main(dirName)  # Вызов основной функции с указанным путем