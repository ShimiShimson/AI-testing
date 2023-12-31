import random
import pygame
import sys

pygame.init()

# Define the size of the world
world_size = (1024, 1024)

screen = pygame.display.set_mode(world_size)

# Create a list to store the grid cells
grid = []

# Generate a reduced number of cells for better performance
num_cells = 50
for i in range(num_cells):
    cell = [random.randint(0, world_size[0]), random.randint(0, world_size[1])]
    grid.append(cell)

# Define the size of each cell
cell_size = 50


# Add content to the world
def generate_landmass(x, y, shape):
    # Generate a random shape for the landmass
    shape = ("oval", "square")
    # Set the size and position of the landmass
    position = (x * cell_size, y * cell_size)
    x_pos, y_pos = position

    # Draw the landmass according to the chosen shape
    if shape == "oval":
        pygame.draw.ellipse(screen, (50, 150, 50), (x_pos, y_pos, 100, 50))
    else:
        pygame.draw.rect(screen, (50, 150, 50), (x_pos, y_pos, 100, 50))

    return shape, position


# Add mountains and oceans
def generate_mountains(x, y):
    # Generate a random shape for the mountain range
    shape = ("lines", "square")
    # Set the size and position of the mountain range
    size = (50, 25)
    position = (x * cell_size, y * cell_size)

    # Draw the mountains according to the chosen shape
    if shape == "lines":
        for i in range(5):
            pygame.draw.line(
                screen,
                (0, 0, 0),
                (position[0] + random.randint(0, size[0]), position[1] + i * 5),
                (
                    position[0] + size[0] - random.randint(0, size[0]),
                    position[1] + i * 5,
                ),
                3,
            )
    else:
        pygame.draw.rect(
            screen, (0, 0, 0), (position[0], position[1], size[0], size[1])
        )

    return shape, position


def generate_oceans(x_pos, y, shape):
    # Generate a random shape for the ocean
    shape = ("rect", "triangle")
    # Set the size and position of the ocean
    size = (100, 50)
    position = (x_pos, y)

    # Draw the oceans according to the chosen shape
    if shape == "rect":
        pygame.draw.rect(screen, (0, 0, 150), position, size)
    else:
        points = [
            (position[0], position[1] + size[1]),
            (position[0] + size[0], position[1] + size[1] / 2),
            (position[0] + size[0] / 2, position[1]),
        ]
        pygame.draw.polygon(screen, (0, 0, 150), points)

    return shape, position


# Add content to the world
for i in range(num_cells):
    # Generate a landmass
    x, y = grid[i]  # Unpack the grid cell tuple
    # Add the shape argument to the generate_landmass() call
    shape, position = generate_landmass(x, y, "oval")

    # Generate fewer mountains and oceans around the landmass for better performance
    for j in range(2):
        shape, position = generate_mountains(
            grid[i][0] + random.randint(-5, 5), grid[i][1] + random.randint(-5, 5)
        )
        grid.append([position[0], position[1]])

        shape, position = generate_oceans(grid[i][0], grid[i][1], "triangle")
        grid.append([position[0], position[1]])

    pygame.display.flip()  # Move this outside the inner loop

# Create a game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()
