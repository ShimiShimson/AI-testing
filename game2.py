import random
import pygame
import sys

pygame.init()
# Define the size of the world
world_size = (1024, 1024)

screen = pygame.display.set_mode(world_size)

# Create a list to store the grid cells
grid = []

# Generate a random number of cells in the grid
num_cells = 100
for i in range(num_cells):
    cell = [random.randint(0, world_size[0]), random.randint(0, world_size[1])]
    grid.append(cell)

# Define the size of each cell
cell_size = 50

# Add content to the world
def generate_landmass(x, y):
    # Generate a random shape for the landmass
    shape = ("oval", "square")
    # Set the size and position of the landmass
    size = (100, 50)
    position = (x * cell_size, y * cell_size)
    return shape, position

# Add mountains and oceans
def generate_mountains(x, y):
    # Generate a random shape for the mountain range
    shape = ("lines", "square")
    # Set the size and position of the mountain range
    size = (100, 50)
    position = (x * cell_size, y * cell_size)
    return shape, position

def generate_oceans(x, y):
    # Generate a random shape for the ocean
    shape = ("rect", "triangle")
    # Set the size and position of the ocean
    size = (100, 50)
    position = (x * cell_size, y * cell_size)
    return shape, position

# Add content to the world
for i in range(num_cells):
    # Generate a landmass
    shape, position = generate_landmass(grid[i][0], grid[i][1])
    # Add the landmass to the grid
    grid.append([position[0] + cell_size, position[1] + cell_size])

    # Generate mountains and oceans around the landmass
    for j in range(5):
        shape, position = generate_mountains(grid[i][0] + random.randint(-5, 5), grid[i][1] + random.randint(-5,5))
        grid.append([position[0], position[1]])
        shape, position = generate_oceans(grid[i][0] + random.randint(-5, 5), grid[i][1] + random.randint(-5, 5))
        grid.append([position[0], position[1]])

# Create a game loop
while True:
    # Check for key presses
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    # Clear the screen and draw the world
    screen.fill((255, 255, 255))
    for cell in grid:
        # Draw the cell's position
        pygame.draw.rect(screen, (0, 0, 0), (cell[0], cell[1], cell_size, cell_size))

    # Update the game state
    pygame.time.Clock().tick(60)

    