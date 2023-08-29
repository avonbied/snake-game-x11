import arcade #imports the library which in this case is arcade
from game import Game 

# Run game here
def main():

    new_game = Game(640, 480, "Snake Game") #size of the arcade window
    arcade.run()


if __name__ == "__main__":
    main()