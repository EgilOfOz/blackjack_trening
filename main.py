import random

kort = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

sum = 0
while True:
    num = random.randint(0, 12)

    print(kort[num])
    if kort[num] == "2":
        sum = sum + 2
    elif kort[num] == "3":
        sum = sum + 3
    elif kort[num] == "4":
        sum = sum + 4
    elif kort[num] == "5":
        sum = sum + 5
    elif kort[num] == "6":
        sum = sum + 6
    elif kort[num] == "7":
        sum = sum + 7
    elif kort[num] == "8":
        sum = sum + 8
    elif kort[num] == "9":
        sum = sum + 9
    elif kort[num] == "10":
        sum = sum + 10
    elif kort[num] == "J":
        sum = sum + 10
    elif kort[num] == "Q":
        sum = sum + 10
    elif kort[num] == "K":
        sum = sum + 10
    elif kort[num] == "A":
        sum = sum + 11
    print(sum)
    if sum == 31:
        print("Du fikk 31!!! Gratulerer")
        break
    elif sum > 31:
        print("Taper...")
        break
    print()
    input()