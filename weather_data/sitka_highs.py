from pathlib import Path
import csv
import matplotlib.pyplot as plt  # type: ignore


path = Path('weather_data/sitka_weather_07-2021_simple.csv')  # Point to specific csv file 
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temps
highs = [] # Create empty list
for row in reader:  # loop through the rows in reader
    high = int(row[4])  # high = to row being converted to ints
    highs.append(high)  # Append high to empty list highs 

# Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

# Format the plot 
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temeprature(F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
