# for loops using Dict
# Author: Éilis Sutton

car = {
    "make" : "Suzuki", 
    "model" : "S-cross", 
    "price" : 10000, 
    "tags" : ["pre-owned", "Best Buy", "Dealer"]
}

#print (car)

#for key in car:
#    print (key, ' has value ', car[key])    # will print out each of the keys and their value

# its neater to use the items
for key, value in car.items():
    print(key,'has a value', value) 