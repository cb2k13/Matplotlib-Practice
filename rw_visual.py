
import matplotlib.pyplot as plt # type: ignore

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:
    # Make a random walk
    rw = RandomWalk()  # Create a random walk and assign it to rw 
    rw.fill_walk()


    # Plot the points in the walk 
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15) # Feed the rw x and y values to scatter()
    ax.set_aspect('equal') # Use set_ascpect() method to specify both axes should have equal spacing between tick marks 
    
    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)
    
    # Remove the axes 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False) # Set the axes to invisble
        
    plt.show()

    keep_running = input("Make another walk? (y/n?): ")
    if keep_running == 'n':
        break
