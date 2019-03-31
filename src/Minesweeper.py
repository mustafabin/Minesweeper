from tkinter import Tk, Canvas, Label
from random import choice
class Minesweeper(object):

    def __init__(self):
        self.newgame = Tk()
        self.newgame.wm_title("MINESWEEPER GAME- Mustafa, Omar, and Renata ")

        self.height = height#400 pixels
        self.width = width#500 pixels
        self.boxwidth = game_width #number of boxes across
        self.boxheight = game_length #number of boxes down
        self.n = bombs
        self.flag_counter = 0
        self.offset = 5
        self.label = Label(master = self.newgame, text = "" , font = ("Times", 20))
        self.flags = self.create_board()     
        self.x = (self.width) // self.boxwidth #20 pixels across per box
        self.y = (self.height) // self.boxheight #20 pixels down per box
        self.mainbox = Canvas(self.newgame, width = width, height = height+self.offset)
        self.mainbox.pack(side = "top")
        #self.mainbox.create_rectangle(5,5, 305,405, outline = "red")
        
        
    def clickmouse(self, event):
        column = (event.x-self.offset) // self.x
        row = (event.y-self.offset) // self.y
        self.uncover_board(column,row)
        if self.end_game(column, row) == True:
            self.label["text"] = "Congrats go get em tiger!! you won :) " 
            self.label.pack(side = "bottom")
            self.mainbox.unbind("<Button-1>")
            self.mainbox.unbind("<Button-2>")
        elif self.end_game(column, row) == False:
            self.label["text"] = "Oh no you lost :( .... you'll get em next time tiger" 
            self.label.pack(side = "bottom")
            self.mainbox.unbind("<Button-1>")
            self.mainbox.unbind("<Button-2>")
            self.display_wholeboard()
            
            
        self.displayboard()
        
       
   
    def displayboard(self):
       offset = self.offset
       for y in range(self.boxheight):
           for x in range(self.boxwidth):
               if (self.board[y][x] == None or self.board[y][x] == -1) and self.flags[y][x] != "f":
                   self.mainbox.create_rectangle(self.x * x+offset, self.y * y+offset, self.x * (x+1)+offset , self.y * (y+1)+offset, fill = "gainsboro")
               elif self.flags[y][x] == "f" and self.flag_counter < self.n +1:
                   self.mainbox.create_rectangle(self.x * x + self.offset, self.y * y +self.offset, self.x * (x+1)+self.offset , self.y * (y+1)+self.offset, fill = "red")
               else:
                   self.mainbox.create_rectangle(self.x * x+offset, self.y * y+offset, self.x * (x+1)+offset , self.y * (y+1)+offset, fill = "sandybrown")
                   if self.board[y][x] != 0:
                       self.mainbox.create_text(self.x * x + offset +self.x//2, self.y * y + offset + self.y // 2, text = str(self.board[y][x]))
                       
    def create_board(self):
        board_to_return = []
        self.board = []
        for h in range(self.boxheight):
            board_to_return_width = []
            self.board_width = []
            for w in range(self.boxwidth):
                board_to_return_width.append(None)
                self.board_width.append(None) #does the horizontal parts of width
            board_to_return.append(board_to_return_width)
            self.board.append(self.board_width) #repeats the horizontal to make it a rectangle with height
        return board_to_return
        
    def make_bombs(self):
        counter = 0
        while counter < self.n:
            x = choice(range(self.boxwidth))# gets a random x coor based on the length of the sub-list
            #print(x)
            y = choice(range(self.boxheight)) # gets a random y coor based on the lenght of the whole board
            #print(y)
            if self.board[y][x] == None:
                self.board[y][x] = -1
                counter += 1   
            
    def uncover_board(self,x,y):
            
        if self.board[y][x] == None:
            self.board[y][x] = self.get_mine_count(x,y)
            if self.board[y][x] == 0:
                for (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]:
                    if self.check_index(x+dx,y+dy):
                        self.uncover_board(x+dx,y+dy)
    def get_mine_count(self,x,y):
            box_value = 0
            for (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]:
                if self.check_index(x+dx,y+dy) and self.board[(y+dy)][(x+dx)] == -1:
                    box_value += 1
            return box_value   
        
    def check_index(self,x,y):
        if x >= 0 and x < self.boxwidth and y >= 0 and y < self.boxheight:
            return True
        return False 
    
      
    def run(self):
        self.create_board()
        self.displayboard()
        self.make_bombs()
        self.mainbox.bind("<Button-1>", self.clickmouse)
        self.mainbox.bind("<Button-2>", self.flag_box) #for macs its button2 for pc its button 3 (i think)
        #self.check_index()
        
        self.newgame.mainloop()
      
    def flag_box(self,event):
        column = (event.x-self.offset) // self.x
        row = (event.y-self.offset) // self.y
        if self.flags[row][column]==None:
            self.flags[row][column] = "f"
        else:
            self.flags[row][column] = None
        self.uncover_board(column, row)
        if self.flag_counter < self.n +10:
            self.mainbox.create_rectangle(self.x * column + self.offset, self.y * row +self.offset, self.x * (column+1)+self.offset , self.y * (row+1)+self.offset, fill = "red")

            self.flag_counter += 1
        self.displayboard()

    def end_game(self,x,y):
        if self.board[y][x] == -1:
            return False
        elif self.countX():     

            return True
            
    def countX(self):
        for row in self.board:
            for ele in row:
                if ele == None:
                    return False
        return True
        
        
        
       
width = 400
height = 500 

# =============================================================================
game_width = int(input("how many boxes across: "))
game_length = int(input("how many boxes down: "))
b = int(input("how many mines do want: "))
# =============================================================================
bombs = b
app = Minesweeper()
app.run()


