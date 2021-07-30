import random
Cchoice = ["rock","paper","scissor"]                     # list of computer
while True:
    print("rock paper scissor game:")
    Youwin,computerwin=0,0
    for i in range(1,6):                                # 5 round game
             print("round",i,"start:")
             print("please select any of one option:")
             print("1.rock","2.paper","3.scissor",sep="\n")     # choice any option
             Yourchoice=int(input())
             if Yourchoice==1:
                 print("you selet rock")
                 Yourchoice = "rock"
             elif Yourchoice ==2:
                 print("you select paper")
                 Yourchoice == "paper"
             elif Yourchoice == 3:
                 print("you select scissor")
                 Yourchoice == "scissor"
             else:
                 print("invalid choice")
                 break

             Computerchoice=random.choice(Cchoice)                # random select by computer
             print("computer select:",Computerchoice)
             if Yourchoice==Computerchoice:
                   Youwin+=1
                   computerwin+=1
                   print("round is drawn.")
             elif (Yourchoice =="paper" and Computerchoice=="rock") or(Yourchoice=="rock" and Computerchoice=="scissor") or (Yourchoice =="scissor" and Computerchoice=="paper"):
                 Youwin+=1
                 print("You win this round")
             else:
                 computerwin+=1
                 print("Computer win this round")
# if your point is more than you win and vice versa

    if Youwin>computerwin:
        print("you win thw match")
        print("score is:","your score:",Youwin, "computer score:",computerwin,sep = " ")
    elif computerwin>Youwin:
        print("you lose the game.computer win the match")
        print("score is:", "your score:", Youwin, "computer score:", computerwin, sep=" ")
    else:
        print("Match Drawn")
        print("score is:", "your score:", Youwin, "computer score:", computerwin, sep=" ")
    user_choice =input("want to play again? (yes/exit)")
    if user_choice =='yes':
        continue
    else:
        break















