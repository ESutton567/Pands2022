# This program add doSave and doLoad to the studentManagement.py from lab 6


import json
from re import S
filename = "studentData.json"

students= []

def displayMenu():
    print("What would you like to do? ")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    print("\t(s) save")
    print("\t(l) load")
    choice = input("Type one letter (a/v/q/s/l):").strip()   # strip() removes spaces at the beginning and at the end of the string
    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name:")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)
    return students

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit): ").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # no error handling
        module["grade"]=int(input("\t\tEnter grade: "))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter the next Module name (blank to quit) ").strip()

    return modules

def displayModules(modules):
    print ("\tName  \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])
    return students

def doSave(students):
    with open(filename, 'wt') as f:
        json.dump(students,f)   # dump the students into the file (f)
    print("saved")
    return students

def doLoad(students):
    with open(filename, "rt") as f:
        return json.load(f)

# make a dict object and map a/v/s/l/q to their respective functions
menuChoice = {
    'a': doAdd,
    'v': doView, 
    's': doSave,
    'l': doLoad,
}

choice = displayMenu()
while(choice != 'q'):
    if choice in menuChoice:
        students = menuChoice[choice](students)        #  menuChoice[choice] maps to a function
    else:
        print("invalid choice try again")    
    
    choice = displayMenu()
    
doSave(students)
print("students saved")
