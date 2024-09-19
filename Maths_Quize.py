# Python project for Maths_Quize 

import random
import time

operator = ['+','-','*']
num_min = int(input("Enter Starting value for operation: "))
num_max = int(input("Enter Ending value for the operation: "))

correct = 0
wrong = 0

def generate_question():
    left = random.randint(num_min,num_max)
    right = random.randint(num_min,num_max)
    opr = random.choice(operator)
    expr = str(left) + " " + opr + " " + str(right) 
    answer = eval(expr)
    return expr,answer



input("Press Enter To Start!")
print("-"*20)
start_time = time.time()
for i in range(10):
    expr,answer = generate_question()
    while True:
        guess = int(input("Problem "+str(i+1)+ ":  "+ expr + " = "))
        print(answer)
        if answer == guess:
            correct+=1
            break
        else:
            wrong+=1
            break
end_time = time.time()
total_time = round(end_time - start_time )
print("-"*20)
print("Nice Work! You Fisnished in ",total_time,"Seconds") 
print("Correct Answer : ",correct)
print("Wrong Answer : ",wrong)




