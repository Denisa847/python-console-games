from src.board import Board

class Play:
    def __init__(self,board):
        self.board=board
        self.direction="up"

    def get_board(self):
        return self.board


    def move_steps(self,n=1):
        for _ in range(n):
            if not self.move_one_step():
                return False

        return True



    def move_one_step(self):
      snake=self.board.snake
      x,y=snake[0]

      if self.direction=="up":
          new_x,new_y=x-1,y
      elif self.direction=="down":
          new_x,new_y=x+1,y
      elif self.direction=="left":
          new_x,new_y=x,y-1
      else:
          new_x,new_y=x,y+1


      if new_x<0 or new_x>=self.board.size or new_y<0 or new_y>=self.board.size:
          print("Hit the wall!")
          return False

      if (new_x,new_y) in snake:
          print("Snake hit itself!")
          return False

      if self.board._board[new_x][new_y]=="a":
         snake=[(new_x,new_y)]+snake
         self.board.snake=snake
         self.board._board[new_x][new_y]="*"
         self.board._board[x][y] = "+"
         self.board.place_apple()
      else:
        last_x, last_y = snake[-1]
        self.board._board[last_x][last_y] = " "
        snake=[(new_x,new_y)]+snake[:-1]
        self.board.snake=snake
        self.board._board[new_x][new_y]="*"
        self.board._board[x][y] = "+"




      return True




    def change_direction(self,new_direction):
        opposite={"left":"right", "up":"down", "down":"up", "right":"left"}
        if new_direction!= opposite[self.direction]:
            self.direction=new_direction
            return True
        else:
            return False








