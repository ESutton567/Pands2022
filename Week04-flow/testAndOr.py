# Messing with 'Ands' and 'Ors'
# Éilis Sutton

number = -1
if ( number >= 0 ) and ( number <= 100) :           # Need the second 'number' here
    print("valid") 

if ( number <= 0 ) and ( number >= 100) :           # This logic is incorrect. As one is true and the other is false
    print("stop")                                   # True and false, and vice versa, is false
else:
    print("go")


if ( number <= 0 ) or ( number >= 100) :           # This works
    isbad = True
    print("stop")                                
else:
    isbad = False
    print("go")