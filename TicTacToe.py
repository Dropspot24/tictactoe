import random
import turtle

#turtle heseg
turtle.title('Tic Tac Toe')

def draw_board():
    
    turtle.forward(300)
    turtle.backward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(300)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(300)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.backward(300)
    
def draw_x(x,y):
    
    turtle.pensize(3)
    turtle.color('blue')
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(0)
    turtle.right(45)
    turtle.forward(90)
    turtle.penup()
    turtle.backward(45)
    turtle.left(90)
    turtle.forward(45)
    turtle.pendown()
    turtle.backward(90)
    turtle.right(45)
    

def draw_circle(x,y):
    
    turtle.color('red')
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    

def draw_horizontal_line(x,y):
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(0)
    turtle.right(90)
    turtle.forward(300)
    turtle.backward(300)
    turtle.right(180)
    

def draw_vertical_line(x,y):
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(0)
    turtle.right(180)
    turtle.forward(300)
    turtle.left(0)
    

def draw_left_angle_line(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(0)
    turtle.right(135)
    turtle.forward(400)
    
###################################
def draw_right_angle_line(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(0)
    turtle.left(135)
    turtle.forward(400)
    
def draw_marker(player, player_pos):
    
    if player_pos == 1 and player == 'o':
        ##circle index 1
        draw_circle(80,50)
    elif player_pos == 2 and player == 'o':
        ##circle index 2
        draw_circle(180,50)
    elif player_pos == 3 and player == 'o':
        ##circle index 3
        draw_circle(280,50)
    elif player_pos == 4 and player == 'o':
        ##circle index 4
        draw_circle(80,-40)
    elif player_pos == 5 and player == 'o':
        ##circle index 5
        draw_circle(180,-40)
    elif player_pos == 6 and player == 'o':
        ##circle index 6
        draw_circle(280,-40)
    elif player_pos == 7 and player == 'o':
        ##circle index 7
        draw_circle(80,-140)
    elif player_pos == 8 and player == 'o':
        ##circle index 8
        draw_circle(180,-140)
    elif player_pos == 9 and player == 'o':
        ##circle index 9
        draw_circle(280,-140)
    
    elif player_pos == 1 and player == 'x':
        #draw x_1
        draw_x(10,10)
    elif player_pos == 2 and player == 'x':
        #draw x_2
        draw_x(110,10)
    elif player_pos == 3 and player == 'x':
        #draw x_3
        draw_x(210,10)
    elif player_pos == 4 and player == 'x':
        #draw x_4
        draw_x(10,-90)
    elif player_pos == 5 and player == 'x':
        #draw x_5
        draw_x(110,-90)
    elif player_pos == 6 and player == 'x':
        #draw x_6
        draw_x(210,-90)
    elif player_pos == 7 and player == 'x':
        #draw x_7
        draw_x(10,-190)
    elif player_pos == 8 and player == 'x':
        #draw x_8
        draw_x(110,-190)
    else:
        #draw x_9
        draw_x(210,-190)
        
##########end turtle section############

board=['*','','','','','','','','','']

vs =''
player1 = ''
player2 = ''
player1_pos = ''
player2_pos = ''
moves_played = 0

def check_emptyspaces():
    check = 0
    for x in range(1,10):
        if board[x] == '':
            check = 1
    
    if check == 1 :
        check = 0
        return True
    else:
        check = 0
        return False
    
def user_input(player):
    a = 0
    if check_emptyspaces() == True :
        
        while type(a) != type('int') :
            try:
                a = int(input("??????????????" + "1-?????? 9-?????? ?????????????? ?????? ?????????????? ???? :"))
                if a > 0 and a <= 9 :
                    return a
                else:
                    print("?????????? ???????? ???????????????? ?????????? ! ?????????? ?????? ?????????????? ???? !")
                    a = None
                    
            except ValueError:
                print("?????????? ???????? ???????????????? ?????????? ! ?????????? ?????? ?????????????? ???? !")
    else:
        print("??????????????")
        
def validate_position(position):
    
    if board[position] == '':
        return True
    
    else:
        return False
    
def check_wins(player):
    if board[1] == player and board[2] == player and board[3] == player:
        draw_horizontal_line(10, 50)
        return True
    elif board[4] == player and board[5] == player and board[6] == player:
        draw_horizontal_line(10, -50)
        return True
    elif board[7] == player and board[8] == player and board[9] == player:
        draw_horizontal_line(10, -150)
        return True
    elif board[1] == player and board[5] == player and board[9] == player:
        draw_left_angle_line(10, 90)
        return True
    elif board[3] == player and board[5] == player and board[7] == player:
        draw_right_angle_line(300, 90)
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        draw_vertical_line(50, 90)
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        draw_vertical_line(150, 90)
        return True
    elif board[3] == player and board[6] == player and board[9] == player:
        draw_vertical_line(250, 90)
        return True
    else:
        return False
    
def update(player, player_pos):
    
    global moves_played 
    
    if moves_played != 9 :
        
        while validate_position(player_pos)!= True:
            
            player_pos = user_input(player)
            validate_position(player_pos)
        
        else:
            
            if check_emptyspaces() == True:
                
                board[player_pos] = player
                draw_marker(player, player_pos)
                #draw()
                moves_played +=1
                
def generate_random():
    
    return random.randint(1,9)

print("----------------Tic Tac Toe ???????????????????? ???????????? ??????????------------")
print('---------------------------??????????-------------------------------')
print('***************************************************************')
print('* ???????????????? ?????????????????? 3 ???????????????????????? ????????????????????                *')
print('* 1-?????? 9-?????? ?????????????? ???????? ???????????? ??????????????                     *')
print('* ???????? ???????? ?????????? 1-?????? ?????????? ???????????? ???????? ?????????? 9 ???????????? ????????????????. *')
print('********************************************')
print('  ???????? ???????? ???????? ?????????????????????? ?????????????? ?????????? ????:'      )
print('-------------------------------------------------')
print('1. ?????????????? VS ??????????????????')
print('2. ?????????????? VS ??????')
print('-------------------------------------------------')

while vs == '' or vs > 2:
    try:
        vs = int(input('???????????????? ???????????????? ?????????????? ???? :'))
        if vs > 0 and vs <=2 :
            
            while player1 != 'x' or player1 != 'o':
                
                player1 = int(input('?????????????? 1 ???????????? ?????????????????????????? ???????????? X ?????????? O :'))
                if player1 == 1 or player1 == 2:
                    if player1 == 'x':
                        player2 = 'o'
                    else:
                        player2 = 'x'
                        
                    print("?????????????? ?????????????? !!! \n")
                    #draw()
                    draw_board()
                    
                    while check_emptyspaces() == True:
                        
                        ###############
                        player1_pos = user_input(player1)
                        update(player1, player1_pos)
                        
                        if check_wins(player1) == True:
                            print('??????????????', player1 , '???????????? !!!!!!!')
                            break
                        
                        
                        
                        #################
                        if vs == 1:
                            
                            player2_pos = generate_random()
                            if moves_played != 9 :
                                
                                while validate_position(player2_pos)!= True:
                                    player2_pos = generate_random()
                                    validate_position(player2_pos)
                                    
                                else:
                                    board[player2_pos] = player2
                                    draw_marker(player2, player2_pos)
                                    moves_played +=1
                                    
                                    if check_wins(player2) == True :
                                        print('??????????????', player2, '???????????? !!!!!!')
                                        break
                                
                        
                        else:
                            player2_pos = user_input(player2)
                            update(player2, player2_pos)
                            
                        #####################
                            if check_wins(player2) == True :
                                print('??????????????', player2, '???????????? !!!!!!')
                                break
                            
                    
                    
                    
                    if check_emptyspaces() != False :
                        print('?????????????? ?????????????? !!!')
                        
                        
                    break
    except ValueError:
        print('???????????????? ???????? ?????????? ?????????? ! ?????????? ?????????????? ???? !')
        
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.write("?????????????????? ?????????????????? !",font=('Arial', 20, 'normal'))
