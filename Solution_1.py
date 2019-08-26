import os
from datetime import datetime

# Targil:
# 1. add to file print the size of each file
# 2. add to file print the last modified of each file
# 3. read input file name from the user - print in which folder it exist, or not exist
#  *etgar read only part of file name or i.e. *.txt
# 4. read extension from the user - print all files ending with this extension and their location

print(os.getcwd())
os.chdir('C:/itay')

def answer1_2():
    for dirpath, dirnames, filenames\
             in os.walk('c:/itay'):
        d1 = dirpath.replace('\\', '/')
        print(f'------- {d1}')
        for d in dirnames:
            print(f'[{d}]')
        for d in filenames:
            size = os.stat(
                os.path.join(dirpath, d)
            ).st_size
            l_mod = os.stat(
                os.path.join(dirpath, d)
            ).st_mtime
            time = datetime.fromtimestamp(l_mod)
            print(f'{d} {size} Bytes ... [{time}]')

def answer3(searchFor):
    for dirpath, dirnames, filenames\
         in os.walk('c:/itay'):
        if searchFor in filenames:
            return f'Found: {dirpath}'
        for n in filenames:
            if n.find(searchFor) >= 0:
                return f'Found: {dirpath} {n}'
    return "Not found"
fname = 'set_exercise.py'
print(answer3(fname))
fname = 'set' # etgar
print(answer3(fname))

def answer4(searchForExt):
    for dirpath, dirnames, filenames\
         in os.walk('c:/itay'):
        for n in filenames:
            if searchForExt == os.path.splitext(n)[1]:
                print (n)

fname = 'set_exercise.py'
answer4(".py")




