import arcade

class Snake():
    def __init__(self, x_init=0, y_init=0):
        self.x_init, self.y_init = x_init, y_init
        # x, y of direction are ints in [-1 ... 1]
        #   - x : -1 is left | 0 is no_change | 1 is right
        #   - y : -1 is down | 0 is no_change | 1 is up
        # 
        # if x is set to -1 or 1 then y = 0
        # if y is set to -1 or 1 then x = 0
        self.direction = (0, 0)

        # This tells the last filled position of the last part of the snake
        #   - Starts by tracking the head
        # o = head, x = prev_part 
        # | o    |    | x o |    |   x |
        # |      | => |     | => |   o | ....
        # 
        # After growing it tracks the last body part
        # - = last_part
        # | - o |    | x - |    |   x |
        # |     | => |   o | => | o - |
        # 
        # This makes it easier to insert another part when growing
        self.prev_part = (x_init, y_init) #where part that grows is at
        self.body = [(x_init, y_init)] #all parts of the snake

    """Game Logic"""
    def move(self): 
        if sum(self.direction) == 0:
            return #no direction means it isn't movin and it's paused
        x, y = [self.head()[i] + self.direction[i] for i in range(2)] #moves head in direction snake is going
        for part_i, part in enumerate(self.body):
            self.prev_part = self.body[part_i]
            self.body[part_i] = (x, y)
            x, y = [i for i in self.prev_part] #moves parts into places of next part

    # [] [] [] [] x
    #
    # -  [] [] [] []
    #
    # [] [] [] [] []
    def grow(self):
        self.body.append(self.prev_part) #body gets attached to previous part

    # Direction Modes
    # 0 : down, 1 : left, 2 : up, 3 : right
    # (0, -1)   (-1, 0)   (0, 1)    (1, 0)
    def set_direction(self, direction_mode):
        if (direction_mode == 5):
            self.direction = (0, 0) #makes sure snake stays in place
        elif (direction_mode % 2):
            self.direction = (direction_mode - 2, 0) 
        else:
            self.direction = (0, direction_mode - 1)
                    #makes sure snake moves one direction at a time
    def head(self):
        return(self.body[0]) #head of the snake

    def get_body(self):
        return(self.body) #returnall parts of the snake

    def get_part(self, i):
        return(self.body[i]) #returns position of a part of the snake

    def __len__(self):
        return(len(self.body)) #return how many parts the snake has

    """Display Info"""
    def clear(self):
        self.prev_part = (self.x_init, self.y_init)
        self.body = [self.prev_part]
        self.direction = (0, 0) #resets the snake starting position with just the head of the snake

    def draw(self):
        for part in self.body:
            arcade.draw_xywh_rectangle_filled(part[0]*16, part[1]*16, 16, 16, arcade.color.BLACK) #draws the snake itself