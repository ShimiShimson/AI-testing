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
    # Set the size and position of the landmass
    size = (100, 50)
    position = (x * cell_size, y * cell_size)
    return "landmass", position

# Add mountains and oceans
def generate_mountains(x, y):
    # Set the size and position of the mountain range
    size = (100, 50)
    position = (x * cell_size, y * cell_size)
    return "mountains", position

def generate_oceans(x, y):
    # Set the size and position of the ocean
    size = (100, 50)
    position = (x * cell_size, y * cell_size)
    return "oceans", position

# Add content to the world
for i in range(num_cells):
    # Generate a landmass
    grid.append(generate_landmass(grid[i][0], grid[i][1]))

    # Generate mountains and oceans around the landmass
    for j in range(5):
        grid.append(generate_mountains(grid[i][0] + random.randint(-5, 5), grid[i][1] + random.randint(-5,5)))
        grid.append(generate_oceans(grid[i][0] + random.randint(-5, 5), grid[i][1] + random.randint(-5, 5)))

# Create a game loop
clock = pygame.time.Clock()
while True:
    # Check for key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen and draw the world
    screen.fill((255, 255, 255))
    for entry in grid:
        if isinstance(entry, int):  # Treat integers as a placeholder for landmass
            obj_type, (position_x, position_y) = "landmass", (entry, 0)
        else:
            obj_type, (position_x, position_y) = entry

        # Draw different shapes and colors based on object type
        if obj_type == "landmass":
            pygame.draw.rect(screen, (0, 255, 0), (position_x, position_y, cell_size, cell_size))
        elif obj_type == "mountains":
            pygame.draw.lines(screen, (255, 0, 0), False, [(position_x, position_y), (position_x + cell_size, position_y)], 2)
        elif obj_type == "oceans":
            pygame.draw.polygon(screen, (0, 0, 255), [(position_x, position_y), (position_x + cell_size, position_y), (position_x + cell_size/2, position_y + cell_size)], 0)

    # Update the game state
    pygame.display.flip()
    clock.tick(60)
