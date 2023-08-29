import arcade
import random
import snake
import apples

class Game(arcade.Window):
    def __init__(self, window_width, window_height, title):
        # sets up the window -got from arcade website
        super().__init__(window_width, window_height, title)
        # Display Variables
        self.window_width, self.window_height = window_width, window_height

        self.unit_row, self.unit_col = window_width//16, window_height//16 #separate the heigh and width into regular parts

        # Logic Variable
        self.score = 0
        self.lives = 3
        self.snake = snake.Snake(self.unit_row//2, self.unit_col//2) #creates snake
        self.apple_list = apples.Apples(self.unit_row, self.unit_col) #creates apples
        # 0: Start, 1: Running, 2: Pause, 3: End
        self.state = 0

        self.set_update_rate(0.12) #how fast game is running

        arcade.set_background_color(arcade.color.ASH_GREY) 
        

    def check_eat(self):
        if self.state in (2,3) or len(self.apple_list) == 0:
            return #if game is paused, ended, or no apples, then it'll skip the whole function


        for apple_i, apple in enumerate(self.apple_list.apple_list):
            if self.snake.head() == apple: #when snake head touches apple
                self.score += 1
                self.apple_list.eat_apple(apple_i)
                self.snake.grow()
                self.apple_list.new_apple(self.snake.get_body()) #makes new apple not on snake

    # New Game
    def new_game(self):
        self.reset()
        self.score = 0
        self.lives =  3
        self.state = 0

    def reset(self):
        self.snake.clear() #snake in center with just the head
        self.apple_list.clear() #one new apple
        self.apple_list.new_apple(self.snake.get_body())
    
    def death(self):
        if self.lives > 1: 
            self.lives -= 1
            self.reset()
        else:
            self.state = 3 #if no lives left then game is ended


    # COLLISIONS
    def isOutOfBoundaries(self, pos):
        if pos[0] in range(0, self.unit_row) and pos[1] in range(0, self.unit_col): #position is tested to check if it's in window
            return False #if it is then false
        return True

    def checkPositionAllowed(self): #checks if snake is dead
        if self.state in (2,3):
            return #if paused or ended, skip this function
        collides_with_body = False

        for i in range(1, len(self.snake)): #checks if snake runs into itself
            if self.snake.head() == self.snake.get_part(i):
                collides_with_body = True
                break
        if (collides_with_body or self.isOutOfBoundaries(self.snake.head())):
            self.death() #if snake runs into wall or itself, it dies

    def on_update(self, delta_time): #redraws snake
        if self.state in (0,1):
            self.snake.move()
            self.check_eat()
            self.checkPositionAllowed() #game logic

    """Game I/O - Display Info"""
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.snake.draw()
        self.apple_list.draw()
        if self.state not in (2,3): #if not paused or ended, it shows score and lives
            stats_overlay(self.width, self.height-20, self.score, self.lives)
        if self.state == 2:
            pause_overlay(self.width//2, 7*self.height//12) #shows that it is paused
        if self.state == 3: #shows game over
            game_over_overlay(self.width//2, 7*self.height//12, self.score)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if self.state == 0 and key in (arcade.key.UP, arcade.key.DOWN, arcade.key.LEFT, arcade.key.RIGHT):
            self.state = 1 #state of game turns to one when a game begins 
            
        if key == arcade.key.P: #p pauses and unpauses the game
            if self.state in (1,2): #toggle math
                self.state = 3 - self.state
            elif self.state == 0: 
                self.state = 2
        elif not self.state in (2,3): #if game is not paused or ended, direction is changed
            if key == arcade.key.DOWN:
                self.snake.set_direction(0)
            elif key == arcade.key.LEFT:
                self.snake.set_direction(1)
            elif key == arcade.key.UP:
                self.snake.set_direction(2)
            elif key == arcade.key.RIGHT:
                self.snake.set_direction(3)
        elif self.state == 3: #if game is ended, pressing space starts a new game
            if key == arcade.key.SPACE:
                self.new_game()

def stats_overlay(width, y, score, lives): #displays score and lives
    arcade.draw_text("Score: %d" % (score), 20, y, arcade.color.ARSENIC, font_size=16)
    arcade.draw_text("Lives %d" % (lives), width-20, y, arcade.color.ARSENIC, font_size=16, anchor_x="right")

def pause_overlay(x, y): #displays the word pause
    arcade.draw_text("PAUSED", x, y,arcade.color.ARSENIC,font_size=40, align="center", anchor_x="center")
    arcade.draw_text("Press P to continue.", x, y-100, arcade.color.ARSENIC, font_size=16, align="center", anchor_x="center")


def game_over_overlay(x, y, score): #displays the game over
    arcade.draw_text("Game Over!\nYou score %d points." % (score), x, y,arcade.color.ARSENIC,font_size=40, align="center", anchor_x="center")
    arcade.draw_text("Press SPACE to start a new game.", x, y-100, arcade.color.ARSENIC, font_size=16, align="center", anchor_x="center")