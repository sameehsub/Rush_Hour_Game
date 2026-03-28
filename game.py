from car import Car
from board import Board
import sys
import json

class Game:
    """
    Add a class description here.
    Write briefly about the purpose of the class.
    """

    def __init__(self, board: Board) -> None:
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code and erase the "pass"
        self.__board = board


    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
       
        
        move_input = input("Choose which colored car to move, and its direction (Color, Direction). Enter '!' to exit game: ")
        if move_input == '!':
            return False  
    
        try:
            car_name, direction = move_input.split(',')
            car_name = car_name.strip().upper()
            direction = direction.strip().lower()
        except ValueError:
            print("Invalid input format. Please enter the color and direction separated by a comma (e.g., R, r).")
            return True  

        if self.__board.move_car(car_name, direction):
            print("Move successful.")
        else:
            print("Move failed. Try a different move.")
    
        
        return True


    def play(self) -> None:
        """
        The main driver of the Game. Manages the game until completion or exit.
        """
        game_on = True
        while game_on:
            print(self.__board)  
            game_on = self.__single_turn()
        print("Game over. Thank you for playing!")


if __name__ == "__main__":
    try:
        with open("car_config.json", "r") as file:
            car_configs = json.load(file)
    except FileNotFoundError:
        print("Error: car_config.json file not found.")
        sys.exit(1)
    
    board = Board()
    
    for car_name, config in car_configs.items():
        car = Car(car_name, config[0], tuple(config[1]), config[2])
        if not board.add_car(car):
            print(f"Failed to add car {car_name} to the board.")
            sys.exit(1)
    
    game = Game(board)
    game.play()
