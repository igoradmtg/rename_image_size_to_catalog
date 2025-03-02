import cv2
import os
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
from collections import Counter

# Каталог по умолчанию
dirNameDefault = r"z:\001\img3"

def process_image(file_path):
    """
    Обрабатывает одно изображение: открывает его с помощью OpenCV, получает размеры и возвращает информацию о файле.
    """
    try:
        image = cv2.imread(file_path)
        if image is not None:
            height, width, _ = image.shape  # Получаем размеры изображения
            return {
                'file': file_path,
                'bname': os.path.basename(file_path),
                'width': width,
                'height': height
            }
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    return None

def renamFilesInDir(dirFiles):
    """
    Функция для обработки файлов в указанном каталоге.
    Определяет размеры изображений и перемещает их в подкаталоги в зависимости от ориентации (ландшафт/портрет).
    """
    # Получаем список файлов в каталоге
    listFiles = [os.path.join(dirFiles, f) for f in os.listdir(dirFiles) if os.path.isfile(os.path.join(dirFiles, f))]
    
    # Обрабатываем изображения параллельно с использованием ProcessPoolExecutor
    filesInfo = []
    with ProcessPoolExecutor(max_workers=4) as executor:  # Ограничиваем количество процессов до 4
        futures = [executor.submit(process_image, file_path) for file_path in listFiles]
        for future in as_completed(futures):
            result = future.result()
            if result:
                filesInfo.append(result)
    
    # Если файлов нет, завершаем функцию
    if not filesInfo:
        return
    
    # Статистика по размерам изображений
    fileStaticWidth = []  # Статистика файлов по ширине (ландшафт)
    fileStaticHight = []  # Статистика файлов по высоте (портрет)
    
    # Собираем статистику по размерам изображений
    for fileInfo in filesInfo:
        if fileInfo['width'] > fileInfo['height']:
            fileStaticWidth.append(f"{fileInfo['width']}x{fileInfo['height']}")
        else:
            fileStaticHight.append(f"{fileInfo['width']}x{fileInfo['height']}")
    
    # Определяем наиболее часто встречающийся размер для ландшафтных изображений
    if fileStaticWidth:
        counter_width = Counter(fileStaticWidth)
        dirNameWidth = counter_width.most_common(1)[0][0]
        print(f"Width statistics: {counter_width}")
    else:
        dirNameWidth = None
    
    # Определяем наиболее часто встречающийся размер для портретных изображений
    if fileStaticHight:
        counter_height = Counter(fileStaticHight)
        dirNameHeight = counter_height.most_common(1)[0][0]
        print(f"Height statistics: {counter_height}")
    else:
        dirNameHeight = None
    
    print(f"Dir name width: {dirNameWidth}")
    print(f"Dir name height: {dirNameHeight}")
    
    # Перемещаем файлы в соответствующие подкаталоги
    for fileInfo in filesInfo:
        if fileInfo['width'] > fileInfo['height']:
            nameDir = dirNameWidth
        else:
            nameDir = dirNameHeight
        
        if nameDir:
            nameDir = os.path.join(dirFiles, nameDir)
            os.makedirs(nameDir, exist_ok=True)
            newFileName = os.path.join(nameDir, fileInfo['bname'])
            os.rename(fileInfo['file'], newFileName)

def main(dirName):
    """
    Основная функция, которая обрабатывает все подкаталоги в указанном каталоге.
    """
    listDirs = [os.path.join(dirName, f) for f in os.listdir(dirName) if os.path.isdir(os.path.join(dirName, f))]
    
    # Обрабатываем каждый подкаталог
    for subdirName in listDirs:
        print(f"Processing directory: {subdirName}")
        renamFilesInDir(subdirName)

if __name__ == '__main__':
    # Настройка парсера аргументов командной строки
    parser = argparse.ArgumentParser(description="Обработка изображений и их сортировка по ориентации.")
    parser.add_argument('--dir', type=str, default=dirNameDefault, help="Каталог для обработки (по умолчанию: z:\\001\\img)")
    
    # Парсинг аргументов
    args = parser.parse_args()
    
    # Если каталог не указан, используем каталог по умолчанию
    dirName = args.dir if args.dir else dirNameDefault
    
    # Запуск основной функции
    main(dirName)