# Python 3.4
import os
from shutil import copyfile

def search(directory):
    x = 0
    for root, subdirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
                 origin = os.path.join(root, file)
                 x += 1
                 output = 'C:/Users/User/Desktop/Output/File_{0}.jpg'.format(x)
                 copyfile(origin, output)
    print('All done!')

search(input('Enter name of directory to copy: '))
