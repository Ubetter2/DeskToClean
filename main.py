import os
import shutil
import sys

desktopDir = "C:/Users/"+str(os.getlogin())+"/Desktop"
deskPath = "C:/Users/"+str(os.getlogin())+"/Desktop/"

desktopFiles = os.listdir(desktopDir)
sele = []
path = os.path.join(deskPath, "allFolders")

if "allFolders" not in desktopFiles:
    os.mkdir(path)

for x in range(0, len(desktopFiles)):
    if "." not in desktopFiles[x]:
        sele.append(desktopFiles[x])
        
for i in range(0, len(sele)):
    shutil.move(deskPath+sele[i], deskPath+"allFolders")
    print("don")
print(sele)