# messing with the os module
# os module allows us to check a file exists or delete a file

import os

filename = 'test.txt'
if os.path.exists(filename):
    print(filename, 'already exists')
    # os.remove(filename)   # to identify the file exists and immediately remove it
else:
    print(filename, 'does not exist do you want to create one?')


