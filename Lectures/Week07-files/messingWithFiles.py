# messing with files

filename = 'test.txt'
with open(filename, 'w+t') as f:
    f.write("Hello World2")        # be careful using write mode - when you change the text here it will wipe the previous entry
    f.seek(0)     # this brings you back to the beginning of the file in order to be able to read in additon to writing
    data = f.readline()
    print(data)

print("done")

#filename = "testread.txt"   # you cannot read from a file that does not exist - we did not create this file
#with open(filename, 'r') as f:
#    data = f.read()
#    print (data)

# ex of how to open large files and only read a line or a line at a time
with open('messingWithFiles.py', 'rt') as f:
    for line in f:
        print (line[:-1])  # [:-1] takes away the last character that python automatically adds (a new line character)
        print (line, end="")        # this is an alternative way oof writing the above line