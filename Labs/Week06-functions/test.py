
def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit): ").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        module["grade"]=int(input("\t\tEnter grade: "))
        modules.append(module)
        moduleName = input("\tEnter the next Module name (blank to quit) ").strip()

    return modules

    