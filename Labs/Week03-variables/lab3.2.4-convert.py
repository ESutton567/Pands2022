# This program converts a float amount in dollars and converts it to an absolute amount in cent
# Author: Éilis Sutton


number = float(input("Enter amount in Dollars: "))
absoluteValue = abs(int(number*100))

print('That amount in cent is {}'.format(absoluteValue))