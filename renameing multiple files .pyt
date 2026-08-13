import os
from pathlib import Path
folder_path = input("Enter the folder path: ")
if not os.path.exists(folder_path):
    print("The specified folder path does not exist.")
else:
    c=0
    dictionary= Path(folder_path)
    for file in dictionary.iterdir():
        c+=1    
        if file.is_file():
            new_name = str(c) + file.suffix
            new_file_path = file.with_name(new_name + file.suffix)
            os.rename(file, new_file_path)
            print(f"Renamed {file.name} to {new_file_path.name}")
