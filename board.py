from typing import Tuple, List, Optional
from car import Car

Coordinates = Tuple[int, int]

class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class.
    """

    def __init__(self) -> None:
        """
        A constructor for a Board object.
        """
        # Note that this function is required in your Board implementation.
        # implement your code and erase the "pass"
        self.board = [["_"] * 7 for _ in range(7)]
        self.board[3].append("E")
        self.cars = {}
        

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string representing the current status of the board.
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        # implement your code and erase the "pass"
        board_str = ""
        for row in self.board:
            row_str = " ".join(row) + "\n"
            board_str += row_str
        return board_str

    def cell_list(self) -> List[Coordinates]:
        """
        This function returns the coordinates of cells in this board.
        :return: list of coordinates.
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        # implement your code and erase the "pass"
        cells = []

        for row in range(7):  
            for col in range(7):
                cells.append((row, col))  
                if row == 3 and col == 6:
                    cells.append((row, col + 1))
        
        return cells

    def possible_moves(self) -> List[Tuple[str, str, str]]:
        """ 
        This function returns the legal moves of all cars in this board.
        :return: list of tuples of the form (name, move_key, description)
                 representing legal moves. The description should briefly
                 explain what is the movement represented by move_key.
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"description"), ('R','r',"description"), ('O','u',"description")]
        # implement your code and erase the "pass"
        moves_list = []
        for car_name, car in self.cars.items():  # Iterate through each car on the board
            possible_moves = car.possible_moves() 
            for move_key, description in possible_moves.items():  
                required_cells = car.movement_requirements(move_key)
                if all(self.is_cell_empty(cell) for cell in required_cells):
                    moves_list.append((car_name, move_key, description))
        return moves_list

    def is_cell_empty(self, cell: Coordinates) -> bool:
        """Check if the specified cell is empty."""
        if cell[0] < 0 or cell[0] >= len(self.board) or cell[1] < 0 or cell[1] >= len(self.board[0]):
            return False  
        return self.board[cell[0]][cell[1]] == "_"

    def cell_content(self, coordinates: Coordinates) -> Optional[str]:
        """
        Checks if the given coordinates are empty.
        :param coordinates: tuple of (row, col) of the coordinates to check.
        :return: The name of the car in "coordinates", None if it's empty.
        """
        # implement your code and erase the "pass"
        row, col = coordinates
        if 0 <= row < len(self.board) and 0 <= col < len(self.board[0]):
            return self.board[row][col] if self.board[row][col] != "_" else None
        return None

    def add_car(self, car: Car) -> bool:
        """
        Adds a car to the game.
        :param car: car object to add.
        :return: True upon success, False if failed.
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        for coord in car.car_coordinates():
            if not self.is_within_bounds(coord) or not self.is_cell_empty(coord):
                return False  
    
        self.cars[car.get_name()] = car
        for coord in car.car_coordinates():
            row, col = coord
            self.board[row][col] = car.get_name()
        return True
    
    def is_within_bounds(self, coord: Coordinates) -> bool:
        row, col = coord
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])

    def move_car(self, name: str, move_key: str) -> bool:
        """
        Moves car one step in a given direction.
        :param name: name of the car to move.
        :param move_key: the key of the required move.
        :return: True upon success, False otherwise.
        """
        
        if name not in self.cars:
            return False

        car = self.cars[name]
        initial_coordinates = car.car_coordinates()
        required_cells = car.movement_requirements(move_key)

        
        if not all(self.is_cell_empty(cell) or self.cell_content(cell) == name for cell in required_cells):
            return False

        
        if not car.move(move_key):
            return False

        
        for coord in initial_coordinates:
            self.board[coord[0]][coord[1]] = "_"
        
        for coord in car.car_coordinates():
            self.board[coord[0]][coord[1]] = name

        return True
    
    def target_location(self) -> Tuple[int, int]:
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return (3, 7)