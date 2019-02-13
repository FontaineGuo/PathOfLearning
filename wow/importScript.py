import zipfile
import shutil

zipf = zipfile.ZipFile('Addons.zip')
zipf.extractall()
print("--------unzip done------------")

print("move the Interface dir")
shutil.move(".\\Interface","E:\\BattleNet\\BattleNetApps\\World of Warcraft\\_retail_")

print("move the WTF dir")
shutil.move(".\\WTF","E:\\BattleNet\\BattleNetApps\\World of Warcraft\\_retail_")
print("done")
