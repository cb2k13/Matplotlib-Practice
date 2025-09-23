
import plotly.express as px  # type: ignore
from die import Die

# Create an instance of Die with the 6 sides 
die = Die() 

# Roll the die 100 times and store results in a list 
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
poss_results = range(1, die.num_sides + 1)
# Loop through possible values then count how many times each number appears in results 
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency) # Append to the empty array of frequencies the frequency 

fig = px.bar(x=poss_results, y=frequencies)
fig.show()