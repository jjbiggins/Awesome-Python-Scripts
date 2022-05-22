import os
import shutil

#The Path of the directory to be sorted
path = 'C:\\Users\\<USERNAME>\\Downloads'
#This populates a list with the filenames in the directory
list_ = os.listdir(path)

#Traverses every file
for file_ in list_:
    name,ext = os.path.splitext(file_)
    print(name)
    #Stores the extension type
    ext = ext[1:]
    #If it is directory, it forces the next iteration
    if ext == '':
        continue
    if not os.path.exists(f'{path}/{ext}'):
        os.makedirs(f'{path}/{ext}')
    shutil.move(f'{path}/{file_}', f'{path}/{ext}/{file_}')
