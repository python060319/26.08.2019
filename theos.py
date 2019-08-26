import os
print(os.getcwd())
os.chdir('C:/itay')
print(os.listdir())
try:
    os.makedirs("test1/test3") # os.mkdir("test1/test2")
except Exception as e:
    print("---- Error making dir")
    print(e)
    print("---------------------")
print("After")

# --not for nested
# os.removedirs("test1")
import shutil
shutil.rmtree("test1")

os.rename("hello.txt", "goodbye.txt")
os.rename("goodbye.txt", "hello.txt")
print(os.stat("hello.txt").st_size)
mod_time = os.stat("hello.txt").st_mtime
from datetime import datetime
print(datetime.now())
print(f'Modification time : {datetime.fromtimestamp(mod_time)}')

for dirpath, dirnames, filenames\
         in os.walk('c:/itay'):
    d1 = dirpath.replace('\\', '/')
    print(f'------- {d1}')
    for d in dirnames:
        print(f'[{d}]')
    for d in filenames:
        print(f'{d}')

# Targil:
# 1. add to file print the size of each file
# 2. add to file print the last modified of each file
# 3. read input file name from the user - print in which folder it exist, or not exist
#  *etgar read only part of file name or i.e. *.txt
# 4. read extension from the user - print all files ending with this extension and their location
