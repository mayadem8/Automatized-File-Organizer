import os
import shutil

desktop_path = os.path.expanduser("~Desktop")

files_by_extension = {}

list_of_files = os.listdir(desktop_path)
for filename in list_of_files:
    file_path = os.path.join(desktop_path, filename)
    
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1]
        if file_extension not in files_by_extension:
            files_by_extension[file_extension] = []
        files_by_extension[file_extension].append(file_path)   

for file_extansion,file_paths in files_by_extension.items(): 
    folder_name = f"{file_extension[1:].upper()} files"
    folder_path = os.path.join(desktop_path,folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for file_path in file_paths:
        shutil.move(file_path, folder_path)


