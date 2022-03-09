# studentManagement.py
# using a module to break up the code

import studentUtil as su

# main program
students = []
choice = su.displayMenu()
while(choice != 'q'):
    if choice == 'a':
        su.doAdd(students)
    elif choice == 'v':
        su.doView (students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice = su.displayMenu()