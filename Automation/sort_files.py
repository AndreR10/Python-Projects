import os
from pathlib import Path
import shutil
import glob


flag = True
while flag:
    path = input("Please enter the folder path: ")
    if path != '':
        flag = False

files = glob.glob(path + "/*")

documents = ['.pdf', '.docx', '.doc', '.txt']
media = ['.jpeg', '.jpg', '.svg', '.png', '.PNG', '.mp4', '.mp3', '.heic']
setupFiles = ['.exe', '.msi']
compressedFiles = ['.zip']
files = ['.apk']


documents_location = path + '/Documents'
media_location = path + '/Media'
setup_files_location = path + '/SetupFiles'
compressed_filesLocation = path + '/CompressedFiles'
files_focation = path + '/Files'

for file in files:
    if os.path.splitext(file)[1] in documents:
        if(os.path.exists(documents_location)):
            shutil.move(file, documents_location)
        else:
            os.mkdir(documents_location)
            shutil.move(file, documents_location)
    if os.path.splitext(file)[1] in media:
        if(os.path.exists(media_location)):
            shutil.move(file, media_location)
        else:
            os.mkdir(media_location)
            shutil.move(file, media_location)
    if os.path.splitext(file)[1] in setupFiles:
        if(os.path.exists(setup_files_location)):
            shutil.move(file, setup_files_location)
        else:
            os.mkdir(setup_files_location)
            shutil.move(file, setup_files_location)
    if os.path.splitext(file)[1] in compressedFiles:
        if(os.path.exists(compressed_filesLocation)):
            shutil.move(file, compressed_filesLocation)
        else:
            os.mkdir(compressed_filesLocation)
            shutil.move(file, compressed_filesLocation)
    if os.path.splitext(file)[1] in files:
        if(os.path.exists(files_focation)):
            shutil.move(file, files_focation)
        else:
            os.mkdir(files_focation)
            shutil.move(file, files_focation)

print("Files sort completed!")
