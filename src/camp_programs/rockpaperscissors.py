import random
score =0
while True:
    random_num = random.randint(1,3)
    computer_answer = ""
    if random_num == 1:
        computer_answer = "rock"
    elif random_num == 2:
        computer_answer = "paper"
    else:
        computer_answer = "scissors"


    userAnswer=input("Enter rock, paper or scissors: ")
    print("Computer chooses " + computer_answer)
    if computer_answer==userAnswer:
        print("its a tie")
    elif computer_answer=="rock" and userAnswer=="paper":
        print("you win!")
        score = score + 1
    elif computer_answer=="scissors" and userAnswer=="rock":
        print("You win!")
        score = score + 1
    elif computer_answer=="paper" and userAnswer=="scissors":
        print("you win!")
        score = score + 1
    else:
        print("you lose")
    print(score)