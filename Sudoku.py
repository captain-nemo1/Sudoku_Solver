#Making a simple 9 by 9 sudoku solver with backtracking algorithm
board1=[]  
a=9
b=9
#For taking elements input
def input1():
    print("Enter elements\nEnter 0 where empty")
    for i in range(a):
        row=[]
        print("Enter element in row "+ str(i+1))
        for j in range(b):
            c=int(input())
            if(c>=0 and c<=9):
                row.append(c)
            else:
                print("Invalid input\nEnter again")
                c=int(input())
                row.append(c)
       
        board1.append(row)    


def solution(board):
    find=find_empty(board)#returns the location that is empty
    if find is False:
        return True
    else:
        row,col=find   
    for i in range(1,10):#to check all value from 1 to 9 on each empty box
            if check(board,i,(row,col))==True: #checks if that particular value of 'i' fits in empty box or not
                board[row][col]=i
                if solution(board): #recursive backtracking call
                           return True
                board[row][col]=0                    
    return False                           
                
                

def check(board,num,pos):
    for i in range(len(board[0])):#checks if that value was already present in the row or not
        if board[pos[0]][i]==num:
            return False

    for i in range(len(board)):#checks if the value was already present in the column or not
        if board[i][pos[1]]==num:
            return False
    x=pos[0]//3#gives floor value after division
    y=pos[1]//3
    
        
    for i in range(x*3,x*3+3):#check if the number comes somewhere in the small 3x3 block
        for j in range(y*3,y*3+3):
            if board[i][j]==num :
                return False                    
    return True #if not found anywhere            
         

def print_board(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("-----------------------")    
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print("|| ", end="")
                
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ",end="")           
 #finds empty location     
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is 0:
                return (i,j)
    return False
            
        
input1()        
print_board(board1)
solution(board1)
print("Solution")
print_board(board1)