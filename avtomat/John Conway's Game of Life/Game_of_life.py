import pygame


cell_size = 16  # cell's size in pixels
map_size = 32  # number of cells in one line
map_width = cell_size * map_size
map_height = cell_size * map_size
alive_image = pygame.image.load("res/alive_16.png")
dead_image = pygame.image.load("res/dead_16.png")


def init_window():
    """This function creates a game window."""
    pygame.init()
    pygame.display.set_mode((map_width, map_height))
    pygame.display.set_caption("Conway's Game of life")


class Cell:
    """This class describes cells."""

    def __init__(self, location, life_status=False):
        """This function creates cell. Cell has 'location' -  list of two coordinates,
        'life status' is 'True' if cell is alive, 'False' if cell is dead,
        'change' is True if cell will change 'life status', False if not.
        """

        self.change = False
        self.life_status = life_status
        self.location = location


class Map:
    """This class describes game map."""

    def __init__(self, file):
        """This function reads map from file and creates list with cells.
        Cells have live status True('1') or False('0').
        """

        self.map = [[None]*map_size for i in xrange(map_size)]

        with open(file, 'r') as map_file:
            map_text = map_file.readlines()

        for i in xrange(map_size):
            for j in xrange(map_size):
                if map_text[i][j] == '1':
                    self.map[i][j] = Cell([i, j], True)
                else:
                    self.map[i][j] = Cell([i, j], False)

    def draw(self, screen):
        """This function draws living and dead cells on map"""
        for y in xrange(map_size):
            for x in xrange(map_size):
                cell = self.map[y][x]
                if cell.life_status == True:
                    screen.blit(alive_image,(x*cell_size, y*cell_size))
                else:
                    screen.blit(dead_image,(x*cell_size, y*cell_size))

    def get_number_of_cells(self,cell):
        """This function gets the number of living cells around a cell."""
        x = cell.location[0]
        y = cell.location[1]
        x_list = [x-1, x, x+1]
        y_list = [y-1, y, y+1]
        number = 0
        for current_x in x_list:
            for current_y in y_list:
                if x-1 >= 0 and x+1 <= 31 and y-1 >= 0 and y+1 <= 31:
                    current_cell = self.map[current_x][current_y]
                    if current_cell.life_status:
                        number += 1
        if cell.life_status:
            return number-1
        else:
            return number

    def set_changes(self):
        """This function updates cells' 'change' according rules:
        1. Dead cell becomes alive if it has three neighbors. (change = True)
        2. Living cell continues to live if it has two or three neighbors. (change = True)
        """

        for i in xrange(map_size):
            for j in xrange(map_size):
                cell = self.map[i][j]
                if cell.life_status:
                    if self.get_number_of_cells(cell) == 3:
                        cell.change = True
                    elif self.get_number_of_cells(cell) == 2:
                        cell.change = True
                    else:
                        cell.change = False
                else:
                    if self.get_number_of_cells(cell) == 3:
                        cell.change = True
                    else:
                        cell.change = False

    def update_map(self):
        """This function changes cells' life status."""
        for line in self.map:
            for cell in line:
                cell.life_status = cell.change


if __name__ == '__main__':
    init_window()
    screen = pygame.display.get_surface()
    game_map = Map('map')
    game_map.draw(screen)
    while 1:
        pygame.time.delay(100)
        game_map.set_changes()
        game_map.update_map()
        game_map.draw(screen)
        pygame.display.update()
