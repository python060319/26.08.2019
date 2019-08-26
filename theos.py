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
        size = os.stat(
            os.path.join(d1, d)
        ).st_size
        print(f'{d} {size} Bytes')

print(f'Path = {os.getenv("PATH")}')
# modify env variable -- watchout!
# os.environ['PATH'] = os.getenv("PATH") + ";c:\python"

# start process
os.startfile("c:/windows/system32/notepad.exe")

import psutil # requires INSTALLATION from Settings!!!

# Iterate over all running process
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        # kill a process
        if proc.name() == "notepad.exe":
            proc.kill()
        print(processName , ' ::: ', processID)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

import stat
fileAttr = os.stat('hello.txt')
# stat.S_IREAD -- read only
os.chmod('hello.txt', stat.S_IREAD)
# stat.S_IWRITE -- read and write
os.chmod('hello.txt', stat.S_IWRITE)

print(os.path.isfile('hello.txt'))
print(os.path.isdir('hello.txt'))
print(os.path.exists('hello.txt'))

