import numpy as np
import matplotlib.pyplot as plt

def plot_shape(points, title):
    plt.figure()
    plt.plot(points[0, :], points[1, :], 'o-')
    plt.title(title)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Define the original shape (a square)
# Each two numbers correspond to a point ex: (1,1) , (-1,1)
# It draws a line between each point
square = np.array([[1, -1, -1, 1, 1],
                   [1, 1, -1, -1, 1]])

triangle = np.array([[0, 2.5, 2.5, 0],
                   [0, 5, 0, 0]])

plot_shape(square, "Original Shape")

plot_shape(triangle, "Triangle")

# Rotation Matrix
def rotation_matrix(degrees):
    radians = np.deg2rad(degrees)
    return np.array([[np.cos(radians), -np.sin(radians)],
                     [np.sin(radians), np.cos(radians)]])

# Scaling Matrix
def scaling_matrix(sx, sy):
    return np.array([[sx, 0],
                     [0, sy]])

# Translation Matrix (homogeneous coordinates)
def translation_matrix(tx, ty):
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])

# Apply Transformation
def apply_transformation(matrix, points):
    if matrix.shape[0] == 3:
        # Convert points to homogeneous coordinates
        ones = np.ones((1, points.shape[1]))
        points_homogeneous = np.vstack([points, ones])
        transformed_points = matrix @ points_homogeneous
        return transformed_points[:2, :]
    else:
        return matrix @ points

# Rotate the square 90 degrees
rotation = rotation_matrix(90)
rotated_square = apply_transformation(rotation, square)
plot_shape(rotated_square, "Rotated Shape (90 degrees)")

# Scale the square by 2 in x and 0.5 in y
scaling = scaling_matrix(2, 0.5)
scaled_square = apply_transformation(scaling, square)
plot_shape(scaled_square, "Scaled Shape (2x, 0.5y)")

# Translate the square by (3, 4)
translation = translation_matrix(3, 4)
translated_square = apply_transformation(translation, square)
plot_shape(translated_square, "Translated Shape (3, 4)")


# The goal of the first activity is to create a simple shape (i.e square)
# Move the square to a certain location
new_square = np.array([[1,1,-1,-1,1],
                       [1,-1,-1,1,1]])

plot_shape(new_square, "Square")

translated_new_square = apply_transformation(translation, new_square)
plot_shape(translated_new_square, "Translated Square (3, 4)")


# The goal of the second activity is to create a pentagon with points at 
# (0,5) , (3.75, 3.75) , (3.75, -2.5) , (-5, -3) , (-5, 2.5)
# move the shape 
# and scale the shape bigger or smaller 
pentagon = np.array([[0, 3.75, 3.75, -5, -5, 0],
                     [5, 3.75, -2.5, -3, 2.5, 5]])

pentagon2 = np.array([[0, 0.951, 0.588, -0.588, -0.951, 0],
                     [1, 0.309, -0.809, -0.809, 0.309, 1]])

plot_shape(pentagon, "Pentagon")
plot_shape(pentagon2, "Pentagon")

translated_pentagon = apply_transformation(translation, pentagon)
plot_shape(translated_pentagon, "Translated Pentagon (3, 4)")

# The goal of the third activity is to create a hexagon with the points at:
# 
# move the shape
# and scale the shape bigger or smaller
# and rotate the shape

hexagon = np.array([[0.5, 1, 0.5, -0.5, -1, -0.5, 0.5],
                     [0, 0.866, 1.732, 1.732, 0.866, 0, 0]])

plot_shape(hexagon, "Hexagon")