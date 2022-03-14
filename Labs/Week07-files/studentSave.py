students= []

def displayMenu():
    print("What would you like to do? ")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()   # strip() removes spaces at the beginning and at the end of the string
    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name:")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)



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

import json
filename = "studentData.json"

def doSave(students):
    with open(filename, 'wt') as f:
        json.dump(students,f)
    print("in save")

choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView (students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice = displayMenu()
    
doSave(students)
print("students saved")
