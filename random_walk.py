from random import choice

class RandomWalk:
    """A class to generate random walks. """

    def __init__(self, num_points=5000):   # Set default number of points in a walk to 5000
        """Initalize attributes of a walk"""
        self.num_points = num_points

        # All walks start at (0, 0)/ make 2 lists to hold x and y axis values and start each walk at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the desired length with correct number of points. 
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go 
            x_direction = choice([1, -1])  # Returns 1 for right movement and -1 for left movement 
            x_distance = choice([0, 1, 2, 3, 4]) # Randomly selects a distance to move in that direction 
            x_step = x_direction * x_distance  # Determine length of each step by multiplying direction by distance chosen 

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)