"""
-----------ULTIMATE TIC TAC TOE-----------
"""

#GLOBAL VARIABLES
rule = -2
current_player = 'X'  #sets current player to X
game_still_playing = True

#main function
def main():
  
    

    #sets board
    board = [["-", "-", "-", "-", "-", "-", "-", "-", "-"] for i in range(9)]

    #displays board
    def display_board(board):
        print(board[0][0] + " | " + board[0][1] + " | " + board[0][2] +
              "  |  " + board[1][0] + " | " + board[1][1] + " | " +
              board[1][2] + "  |  " + board[2][0] + " | " + board[2][1] +
              " | " + board[2][2])
        print(board[0][3] + " | " + board[0][4] + " | " + board[0][5] +
              "  |  " + board[1][3] + " | " + board[1][4] + " | " +
              board[1][5] + "  |  " + board[2][3] + " | " + board[2][4] +
              " | " + board[2][5])
        print(board[0][6] + " | " + board[0][7] + " | " + board[0][8] +
              "  |  " + board[1][6] + " | " + board[1][7] + " | " +
              board[1][8] + "  |  " + board[2][6] + " | " + board[2][7] +
              " | " + board[2][8])
        print("---------  |  ---------  |  ---------  ")
        print("---------  |  ---------  |  ---------  ")
        print(board[3][0] + " | " + board[3][1] + " | " + board[3][2] +
              "  |  " + board[4][0] + " | " + board[4][1] + " | " +
              board[4][2] + "  |  " + board[5][0] + " | " + board[5][1] +
              " | " + board[5][2])
        print(board[3][3] + " | " + board[3][4] + " | " + board[3][5] +
              "  |  " + board[4][3] + " | " + board[4][4] + " | " +
              board[4][5] + "  |  " + board[5][3] + " | " + board[5][4] +
              " | " + board[5][5])
        print(board[3][6] + " | " + board[3][7] + " | " + board[3][8] +
              "  |  " + board[4][6] + " | " + board[4][7] + " | " +
              board[4][8] + "  |  " + board[5][6] + " | " + board[5][7] +
              " | " + board[5][8])
        print("---------  |  ---------  |  ---------  ")
        print("---------  |  ---------  |  ---------  ")
        print(board[6][0] + " | " + board[6][1] + " | " + board[6][2] +
              "  |  " + board[7][0] + " | " + board[7][1] + " | " +
              board[7][2] + "  |  " + board[8][0] + " | " + board[8][1] +
              " | " + board[8][2])
        print(board[6][3] + " | " + board[6][4] + " | " + board[6][5] +
              "  |  " + board[7][3] + " | " + board[7][4] + " | " +
              board[7][5] + "  |  " + board[8][3] + " | " + board[8][4] +
              " | " + board[8][5])
        print(board[6][6] + " | " + board[6][7] + " | " + board[6][8] +
              "  |  " + board[7][6] + " | " + board[7][7] + " | " +
              board[7][8] + "  |  " + board[8][6] + " | " + board[8][7] +
              " | " + board[8][8])

    #run game

    def play_game():
        global game_still_playing
        global current_player
        
         #game is playing while True
        polje1 = board[0]
        polje2 = board[1]
        polje3 = board[2]
        polje4 = board[3]
        polje5 = board[4]
        polje6 = board[5]
        polje7 = board[6]
        polje8 = board[7]
        polje9 = board[8]

       

        
        display_board(board)#displays board

        while game_still_playing:
          global rule

          print()
          
         
          
          
        
          print(f"Current player: {current_player}")  #shows current player
          print()
          print("Choose a field from 1-9 then choose position from 1-9") 
          

          if rule != -2:
            print("The field must be: ",rule+1) 
          elif rule == -2:
            print("You can choose any field that is not filled!")
          

          #rules of a game
          valid = True
          
          num = [i for i in range(9)]
        
          
    
          while valid:
            print()
            print()
            #["-","X","X"]
            field = int(input("Field: ")) - 1
            position = int(input("Position: ")) - 1
        
            
            

            if field not in num or position not in num:
              print("Wrong input!\n")

            elif board[field][position] != "-":
              print("Wrong input!\n")
          
            elif (rule == 0 and field != 0):
              print("Wrong input!\n")
            elif (rule == 1 and field != 1):
              print("Wrong input!\n")
            elif (rule == 2 and field != 2):
              print("Wrong input!\n")
            elif (rule == 3 and field != 3):
              print("Wrong input!\n")
            elif (rule == 4 and field != 4):
              print("Wrong input!\n")
            elif (rule == 5 and field != 5):
              print("Wrong input!\n")
            elif (rule == 6 and field != 6):
              print("Wrong input!\n")
            elif (rule == 7 and field != 7):
              print("Wrong input!\n")
            elif (rule == 8 and field != 8):
              print("Wrong input!\n")

            
            elif rule == -2:
              valid = False
              
            else:
              valid =False
          
            

          board[field][position] = current_player  #on that field and position place X or O
           
          wins()






            
          if position == 0  and (polje1 not in [["X" for i in range(9)],["O" for i in range(9)]]):
            rule = 0
          
          elif position == 1  and polje2 not in [["X" for i in range(9)],["O" for i in range(9)]]:
            rule = 1
          
          elif position == 2 and polje3 not in [["X" for i in range(9)],["O" for i in range(9)]]:
            rule = 2
          elif position == 3 and  polje4 not in [["X" for i in range(9)],["O" for i in range(9)]]:
            rule = 3
          elif position == 4  and polje5 not in [["X" for i in range(9)],["O" for i in range(9)]]:
            rule = 4
          elif position == 5 and  polje6 not in [["X" for i in range(9)],["O" for i in range(9)]]:
            rule = 5
          elif position == 6 and polje7 not in [["X" for i in range(9)],["O" for i in range(9)]]:
            rule = 6
          elif position == 7 and  polje8 not in [["X" for i in range(9)],["O" for i in range(9)]]:

            rule = 7
          elif position ==8 and  polje9 not in [["X" for i in range(9)],["O" for i in range(9)]]:
            rule = 8
          else:
            rule = -2
             

              


          display_board(board)



          #switching player X to O 
          if current_player == "X":
                  current_player = "O"
          elif current_player == "O":
                  current_player = "X"

          
    

    def wins():
            global current_player
            polje1 = board[0]
            polje2 = board[1]
            polje3 = board[2]
            polje4 = board[3]
            polje5 = board[4]
            polje6 = board[5]
            polje7 = board[6]
            polje8 = board[7]
            polje9 = board[8]
          


            if polje1 not in[["X" for i in range(9)],["O" for i in range(9)]]:
                  #rows
                  if (polje1[0] == polje1[1] == polje1[2] !="-") or (polje1[3] == polje1[4] == polje1[5] != "-") or (polje1[6] == polje1[7] == polje1[8] != "-"):
                    for i in range(9):
                        polje1[i] = current_player
                    
                  #cols
                  elif (polje1[0] == polje1[3] == polje1[6] !="-") or (polje1[1] == polje1[4] == polje1[7] != "-") or (polje1[2] == polje1[5] == polje1[8] != "-"):
                    for i in range(9):
                        polje1[i] = current_player
                    
                  #diagonals
                  elif (polje1[0] == polje1[4] == polje1[8] !="-") or (polje1[2] == polje1[4] == polje1[6] != "-"):
        
                    for i in range(9):
                        polje1[i] = current_player
                    
                  

                #for second SMALL field
            if polje2 not in [["X" for i in range(9)],["O" for i in range(9)]]:
                  #rows
                  if (polje2[0] == polje2[1] == polje2[2] !=
                        "-") or (polje2[3] == polje2[4] == polje2[5] != "-") or (
                            polje2[6] == polje2[7] == polje2[8] != "-"):

                        for i in range(9):
                            polje2[i] = current_player

                        


                  elif (polje2[0] == polje2[3] == polje2[6] !="-") or (polje2[1] == polje2[4] == polje2[7] != "-") or (polje2[2] == polje2[5] == polje2[8] != "-"):
                    for i in range(9):
                        polje2[i] = current_player
                  
                  #diagonals
                  elif (polje2[0] == polje2[4] == polje2[8] !="-") or (polje2[2] == polje2[4] == polje2[6] != "-"):
        
                    for i in range(9):
                        polje2[i] = current_player
                    

                
                #for third SMALL field
            if polje3 not in [["X" for i in range(9)],["O" for i in range(9)]]:
                  #rows
                  if (polje3[0] == polje3[1] == polje3[2] !=
                        "-") or (polje3[3] == polje3[4] == polje3[5] != "-") or (
                            polje3[6] == polje3[7] == polje3[8] != "-"):

                      for i in range(9):
                          polje3[i] = current_player
                      
                  elif (polje3[0] == polje3[3] == polje3[6] !="-") or (polje3[1] == polje3[4] == polje3[7] != "-") or (polje3[2] == polje3[5] == polje3[8] != "-"):
                    for i in range(9):
                        polje3[i] = current_player
                    
                  #diagonals
                  elif (polje3[0] == polje3[4] == polje3[8] !="-") or (polje3[2] == polje3[4] == polje3[6] != "-"):
        
                    for i in range(9):
                        polje3[i] = current_player
                    

                #for foruth SMALL field
            if polje4 not in [["X" for i in range(9)],["O" for i in range(9)]]:
                  #rows
                  if (polje4[0] == polje4[1] == polje4[2] !=
                        "-") or (polje4[3] == polje4[4] == polje4[5] != "-") or (
                            polje4[6] == polje4[7] == polje4[8] != "-"):

                      for i in range(9):
                          polje4[i] = current_player
                      
                  elif (polje4[0] == polje4[3] == polje4[6] !="-") or (polje4[1] == polje4[4] == polje4[7] != "-") or (polje4[2] == polje4[5] == polje4[8] != "-"):
                    for i in range(9):
                        polje4[i] = current_player
                    

                  #diagonals
                  elif (polje4[0] == polje4[4] == polje4[8] !="-") or (polje4[2] == polje4[4] == polje4[6] != "-"):
        
                    for i in range(9):
                        polje4[i] = current_player
                    

                    
                #for fifth SMALL field
            if polje5 not in [["X" for i in range(9)],["O" for i in range(9)]]:
                  #rows
                  if (polje5[0] == polje5[1] == polje5[2] !=
                        "-") or (polje5[3] == polje5[4] == polje5[5] != "-") or (
                            polje5[6] == polje5[7] == polje5[8] != "-"):

                      for i in range(9):
                          polje5[i] = current_player
                      
                  elif (polje5[0] == polje5[3] == polje5[6] !="-") or (polje5[1] == polje5[4] == polje5[7] != "-") or (polje5[2] == polje5[5] == polje5[8] != "-"):
                    for i in range(9):
                        polje5[i] = current_player
                    
                  #diagonals
                  elif (polje5[0] == polje5[4] == polje5[8] !="-") or (polje5[2] == polje5[4] == polje5[6] != "-"):
        
                    for i in range(9):
                        polje5[i] = current_player
                    
                
                #for sixth SMALL field
            if polje6 not in [["X" for i in range(9)],["O" for i in range(9)]]:
                  #rows
                  if (polje6[0] == polje6[1] == polje6[2] !=
                        "-") or (polje6[3] == polje6[4] == polje6[5] != "-") or (
                            polje6[6] == polje6[7] == polje6[8] != "-"):

                      for i in range(9):
                          polje6[i] = current_player
                      

                  elif (polje6[0] == polje6[3] == polje6[6] !="-") or (polje6[1] == polje6[4] == polje6[7] != "-") or (polje6[2] == polje6[5] == polje6[8] != "-"):
                    for i in range(9):
                        polje6[i] = current_player
                  
                  #diagonals
                  elif (polje6[0] == polje6[4] == polje6[8] !="-") or (polje6[2] == polje6[4] == polje6[6] != "-"):
        
                    for i in range(9):
                        polje6[i] = current_player
                  

                #for seventh SMALL field
            if polje7 not in [["X" for i in range(9)],["O" for i in range(9)]]:
                  if (polje7[0] == polje7[1] == polje7[2] !=
                        "-") or (polje7[3] == polje7[4] == polje7[5] != "-") or (
                            polje7[6] == polje7[7] == polje7[8] != "-"):

                      for i in range(9):
                          polje7[i] = current_player
                    

                  elif (polje7[0] == polje7[3] == polje7[6] !="-") or (polje7[1] == polje7[4] == polje7[7] != "-") or (polje7[2] == polje7[5] == polje7[8] != "-"):
                    for i in range(9):
                        polje7[i] = current_player
                  
                  #diagonals
                  elif (polje7[0] == polje7[4] == polje7[8] !="-") or (polje7[2] == polje7[4] == polje7[6] != "-"):
        
                    for i in range(9):
                        polje7[i] = current_player
                    

                #for eight SMALL field
            if polje8 not in [["X" for i in range(9)],["O" for i in range(9)]]:
                  #rows
                  if (polje8[0] == polje8[1] == polje8[2] !=
                        "-") or (polje8[3] == polje8[4] == polje8[5] != "-") or (
                            polje8[6] == polje8[7] == polje8[8] != "-"):

                      for i in range(9):
                          polje8[i] = current_player
                      

                  elif (polje8[0] == polje8[3] == polje8[6] !="-") or (polje8[1] == polje8[4] == polje8[7] != "-") or (polje8[2] == polje8[5] == polje8[8] != "-"):
                    for i in range(9):
                        polje8[i] = current_player
                  
                  #diagonals
                  elif (polje8[0] == polje8[4] == polje8[8] !="-") or (polje8[2] == polje8[4] == polje8[6] != "-"):
        
                    for i in range(9):
                        polje8[i] = current_player
                    

                #for ninth SMALL field
            if polje9 not in [["X" for i in range(9)],["O" for i in range(9)]]:
                  #rows
                  if (polje9[0] == polje9[1] == polje9[2] !=
                        "-") or (polje9[3] == polje9[4] == polje9[5] != "-") or (
                            polje9[6] == polje9[7] == polje9[8] != "-"):

                      for i in range(9):
                          polje9[i] = current_player
                      
                  elif (polje9[0] == polje9[3] == polje9[6] !="-") or (polje9[1] == polje9[4] == polje9[7] != "-") or (polje9[2] == polje9[5] == polje9[8] != "-"):
                    for i in range(9):
                        polje9[i] = current_player
                  

                  #diagonals
                  elif (polje9[0] == polje9[4] == polje9[8] !="-") or (polje9[2] == polje9[4] == polje9[6] != "-"):
        
                    for i in range(9):
                        polje9[i] = current_player
                    

                #for  BIG field

            if (polje1 == polje2== polje3 != ["-" for i in range(9)]) or (polje4 == polje5== polje6 != ["-" for i in range(9)]) or (polje7 == polje8== polje9 !=["-" for i in range(9)]):
                  winner = current_player
                  print("\nWinner is ",winner)
                  game_still_playing = False #ending game

            elif (polje1 == polje4 == polje7 !=["-" for i in range(9)]) or (polje2 == polje5== polje8 != ["-" for i in range(9)]) or (polje3 == polje6== polje9 != ["-" for i in range(9)]):
                  winner = current_player
                  print("\nWinner is ",winner)
                  game_still_playing = False #ending game

            elif (polje1 == polje5== polje9 != ["-" for i in range(9)]) or (polje3 == polje5 == polje7 != ["-" for i in range(9)]):  
                  winner = current_player
                  print("\nWinner is ",winner)
                  print()
                  print()
                  game_still_playing = False #ending game
      

        
    
    play_game()  #run game






main()
