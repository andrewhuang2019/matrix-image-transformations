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
square = np.array([[1, -1, -1, 1, 1],
                   [1, 1, -1, -1, 1]])

plot_shape(square, "Original Shape")

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