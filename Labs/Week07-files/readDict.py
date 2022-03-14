# This program reads in a dict object from a file
# Author: Éilis Sutton

import json
filename = "testdict.json"

def readDict():
    # this will throw an error if the file does not exist
    # it should readily just return an empty dict
    # we can do this later
    with open(filename) as f:
        return json.load(f)

# test this function
somedict = readDict()
print(somedict)