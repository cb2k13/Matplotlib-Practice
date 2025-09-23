import matplotlib.pyplot as plt # type: ignore

# Create the list with data 
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Call subplots() funcion
# fig represents entire figure and ax represents single plot
# in the figure 
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)


# Set chart title and label axises
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick labels 
ax.tick_params(labelsize=14)

# function to show and display the plot 
plt.show()
