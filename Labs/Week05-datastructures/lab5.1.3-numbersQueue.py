# This program puts 10 random numbers into a queue(list), the
# program should then output all the values in the queue, then take the
# numbers from the queue one at a time, print it and the current numbers still
# in the queue

import random
queue = []
numberofNumbers=10
rangeTo=100

print (queue)

for n in range(0,numberofNumbers):
    queue.append(random.randint(0,rangeTo))

while len(queue) !=0:
    currentNumber = queue.pop(0)            # the command pop(0) takes the first element out of a list
    print ("current Number is {} and the queue is {} ".format(currentNumber, queue))

print ("The queue is now empty")
