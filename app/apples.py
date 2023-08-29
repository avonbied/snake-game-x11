import arcade
import random #random functions

class Apples():

    def __init__(self, max_x=0, max_y=0): #creates new apple
        self.apple_list = [] 
        self.row_size = max_x #shows max of x-axis
        self.column_size = max_y #shows max of y-axis
        if self.row_size * self.column_size:
            self.new_apple() #generates new apple on start

    """Game Logic"""
    def new_apple(self, snake_list=[]): #new apple takes all snake positions
        if len(snake_list) >= self.row_size * self.column_size:
            return #if snake is bigger than all possible places that apples can be, then skip this function
        # x: random (left_bound, right_bound)
        # y: random (top_bound, bottom_bound)
        apple = (random.randint(0, self.row_size-1), random.randint(0, self.column_size-1)) #apple has position that is random between 0 and one less than highest
        block_list = snake_list + self.apple_list #block list is where all places snake and apples are
        for block in block_list:
            if block == apple: #sees if random apple is on top of any og block spots
                apple = (random.randint(0, self.row_size-1), random.randint(0, self.column_size-1))  #regenerates apple
        self.apple_list.append(apple) #puts apple on list

    def eat_apple(self, apple_i):
        self.apple_list.pop(apple_i) #removes an apple after being eaten

    def __len__(self):
        return(len(self.apple_list)) #returns how many apples 

    """Display Info"""
    def clear(self):
        self.apple_list = [] #resets apple to 0

    def draw(self):
        for apple in self.apple_list:

            arcade.draw_circle_filled(apple[0]*16+8, apple[1]*16+8, 8, arcade.color.RADICAL_RED) #draws all apples
