import random

'''
-1 for paper
0 for rock
1 for scissor
'''

def game():
    computer = random.choice([-1,0,1])
    your_input = input('''r  -----> Rock 
p  -----> Paper
s  -----> scissor 
now enter your choice: ''')

    user_dic = {"p": -1, "r": 0, "s":1 }
    you_dic = {-1:"Paper",0:"Rock",1: "Scissor"}

    you = user_dic[your_input]

    print(f"you choose {you_dic[you]} \ncomputer choose {you_dic[computer]}")

    if (you == computer ):
        print("its a Draw ")
    else :
        if(computer == -1 and you == 0):
            print("you Won!")
        elif(computer == -1 and you == 1):
            print("you Lose!")
        elif(computer == 0 and you == -1):
            print("you Won!")
        elif(computer == 0 and you == 1):
            print("you Lose!")
        elif(computer == 1 and you == -1):
            print("you Lose!")
        elif(computer == 1 and you == 0):
            print("you Won!")
        else:
            print("you did something wronge")

while True :
    game()
    user = input("Want to play game again (yes/no) : ").lower()
    if (user != "yes"):
        print("No problem this was nice playing with you 😊😊")
        break
