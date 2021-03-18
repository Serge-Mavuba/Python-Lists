# Lists are built-in data structure for storing and accesssing objects
# which belong in a specific sequence.
# There are 2 ways to create a list:
#   1) by using the list constructor: Example = list() 
#   2) by using brackets:             Example = []

# You can create a list and prepopulate it with values/elements
#   Consider the list PRIMES with values 2,3,5,7,11,13
PRIMES = [2,3,5,7,11,13]
print(PRIMES)
#The list should print as follow [2,3,5,7,11,13]

#Use append command line to add new value to the end of the list
PRIMES = [2,3,5,7,11,13]
PRIMES.append(17)
PRIMES.append(19)
print(PRIMES)