
import matplotlib.pyplot as plt  # type: ignore

# Lists of x and y values
x_values = range(1, 1001) # Range of x values
y_values = [x**2 for x in x_values] # Generate y values by looping through x values 

plt.style.use('seaborn') # Style to use 
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color='red', s=10) # Pass it to scatter()

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis 
ax.axis([0, 1100, 0, 1_100_000])  # axis() method to specify range for each axis 

# Set tick size of tick labels
ax.ticklabel_format(style='plain')

plt.show() 