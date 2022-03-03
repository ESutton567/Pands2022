# Messing with dictionaries
# Author: Éilis Sutton

car = {
    "make"  : "ford",
    "model" : "modeo",
    "year"  : 2006,
    "owner" : {             # want to store both name and driver number under 'owner'
        "name" : "andrew" ,               # this doesn't need to be on a new line but it's easier to read if so
        "driver-number" : 1123
    }
}

attr = "make"          # attribute
print (car[attr])
print (car["owner"]["name"])

