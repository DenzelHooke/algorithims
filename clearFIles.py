import os

rootDir = 'D:/SteamLibrary/steamapps/common/Red Dead Redemption 2'
file_names = 'C:/Users/Denze/Documents/rdr2_mod_file_names.txt'

def clear_rdr2_files(rootDir, fileNames):
    file_names = []
    count = 0
    with open(fileNames, 'r') as f:
        for name in f:
            name = name.split('\n')[0]
            
            if name == '*root dir:':
                continue
            file_names.append(name)


    for file_name in os.listdir(rootDir):
        if file_name in file_names:
            os.remove(f'{rootDir}/{file_name}')
    # print(file_names)



clear_rdr2_files(rootDir, file_names)
