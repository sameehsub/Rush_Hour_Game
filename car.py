from typing import Tuple, List, Dict

Coordinates = Tuple[int, int]

class Car:
    """
    Add a class description here.
    Write briefly about the purpose of the class.
    """
    VERTICAL = 0
    HORIZONTAL = 1

    def __init__(self, name: str, length: int, location: Coordinates, 
                 orientation: int) -> None:
        """
        A constructor for a Car object.
        :param name: A string representing the car's name.
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head location (row,col).
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL).
        """
        # Note that this function is required in your Car implementation.
        # implement your code and erase the "pass"
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self) -> List[Coordinates]:
        """
        :return: A list of coordinates the car is in.
        """
        # implement your code and erase the "pass"
        car_coordinates = []
        for i in range(self.__length):
            if self.__orientation == Car.HORIZONTAL:
                car_coordinates.append((self.__location[0], self.__location[1] + i))
            if self.__orientation == Car.VERTICAL:
                car_coordinates.append((self.__location[0] + i, self.__location[1]))
        return car_coordinates
    
    def possible_moves(self) -> Dict[str, str]:
        """
        :return: A dictionary of strings describing possible movements 
                 permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings to describe each movements.
        # For example: a car that supports the commands 'f', 'd', 'a' may return
        # the following dictionary:
        # {'f': "cause the car to fly and reach the Moon",
        #  'd': "cause the car to dig and reach the core of Earth",
        #  'a': "another unknown action"}
        #
        # implement your code and erase the "pass"
        moves = {}
        if self.__orientation == Car.HORIZONTAL:
            moves['l'] = "Move left by one grid space"
            moves['r'] = "Move right by one grid space"
        elif self.__orientation == Car.VERTICAL:
            moves['u'] = "Move up by one grid space"
            moves['d'] = "Move down by one grid space"
        return moves

    def movement_requirements(self, move_key: str) -> List[Coordinates]:
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for 
                 this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        required_cells = []
        if self.__orientation == Car.HORIZONTAL:
            if move_key == 'l': 
                if self.__location[1] > 0:  
                    required_cells.append((self.__location[0], self.__location[1] - 1))
            elif move_key == 'r':  
                required_cells.append((self.__location[0], self.__location[1] + self.__length))
        elif self.__orientation == Car.VERTICAL:
            if move_key == 'u':  
                if self.__location[0] > 0:
                    required_cells.append((self.__location[0] - 1, self.__location[1]))
            elif move_key == 'd':  
                required_cells.append((self.__location[0] + self.__length, self.__location[1]))
        return required_cells

    def move(self, move_key: str) -> bool:
        """
        This function moves the car.
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise.
        """
        if self.__orientation == Car.HORIZONTAL:
            if move_key == 'l':
                
                if self.__location[1] > 0:
                    self.__location = (self.__location[0], self.__location[1] - 1)
                    return True
                else:
                    return False
            elif move_key == 'r':
                
                self.__location = (self.__location[0], self.__location[1] + 1)
                return True

        elif self.__orientation == Car.VERTICAL:
            if move_key == 'u':
                
                if self.__location[0] > 0:
                    self.__location = (self.__location[0] - 1, self.__location[1])
                    return True
                else:
                    return False
            elif move_key == 'd':
                
                self.__location = (self.__location[0] + 1, self.__location[1])
                return True

        return False

    def get_name(self) -> str:
        """
        :return: The name of this car.
        """
        # implement your code and erase the "pass"
        return self.__name
