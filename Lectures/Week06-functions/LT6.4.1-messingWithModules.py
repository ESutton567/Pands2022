# Messing with modules
# anaconda has installed a lot of modules already onto the machine

from constraint import *   # use pip install to download constraint

import nltk

import math

var  = math.cos(3.14)    # Get the function cos out of the math module
print (var)

# alternative way of doing it
from math import cos  
var  = cos(3.14)    # Get the function cos out of the math module
print (var)