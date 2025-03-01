
class Segments:
    def __init__(self, upper:int, right_up: int, right_down: int, down: int, left_down: int, left_up: int, middle: int ,switcher: input):
        self.__board = [[" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "]]
        self.__upper = upper
        self.__right_up = right_up
        self.__right_down = right_down
        self.__down = down
        self.__middle = middle
        self.__left_up = left_up
        self.__left_down = left_down
        self.__switcher = switcher
    
    
    def upper_on(self):
        if self.__upper == 1 and self.__switcher == 1:
            for number in range(len(self.__board[0])):
                self.__board[0][number] = "#"
            
        
                
    def right_up_on(self):
        if self.__right_up == 1 and self.__switcher == 1:
            self.__board[0][3] = "#"
            self.__board[1][3] = "#"
            self.__board[2][3] = "#"
            
    def right_down_on(self):
        if self.__right_down == 1 and self.__switcher == 1:
            self.__board[3][3] = "#"
            self.__board[4][3] = "#"
            self.__board[2][3] = "#"
            
    def down_on(self):
        if self.__down == 1 and self.__switcher == 1:
            print(self.__down)
            for number in range(4):
                self.__board[4][number] = "#" 
        
                
    def middle_on(self):
        if self.__middle == 1 and self.__switcher == 1:
            for number in range(len(self.__board[0])):
                self.__board[2][number] = "#"
                
    def left_up_on(self):
       if self.__left_up == 1 and self.__switcher == 1:
            self.__board[0][0] = "#"
            self.__board[1][0] = "#"
            self.__board[2][0] = "#" 
                   
    def left_down_on(self):
       if self.__left_down == 1 and self.__switcher == 1:
            self.__board[3][0] = "#"
            self.__board[4][0] = "#"
            self.__board[2][0] = "#" 
            
    def get_board(self):
        return self.__board
    
segments = Segments(0,0,0,1,1,1,1,1)
segments.down_on()
owner = segments.get_board()

    
        


            
    
    
                
            
        
    
            
            
        
         