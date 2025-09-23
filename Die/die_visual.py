from die import Die

# Create an instance of Die with the 6 sides 
die = Die() 

# Roll the die 100 times and store results in a list 
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results) # print the list of the result of each roll 