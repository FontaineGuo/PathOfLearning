import zipfile
import shutil

zipf = zipfile.ZipFile('Addons.zip')
zipf.extractall()
print("--------unzip done------------")

print("move the Interface dir")
shutil.move(".\\Interface","C:\\Users\\Fonta\\Desktop\\Temp")

print("move the WTF dir")
shutil.move(".\\WTF","C:\\Users\\Fonta\\Desktop\\Temp")
print("done")