import time

q=[]
start_time=[]
end_time=[]
score=0
answer=["11","0","True","True","24"]

def func(seconds):
    while seconds>0:
        print("Loading......Please Wait")
        time.sleep(2)
        seconds=seconds-1
        break

def func1(seconds):
    while seconds>0:
        print(f"{seconds}")
        time.sleep(1)
        seconds=seconds-1
        if seconds==0:
            print("You can start your exam Now!")

func(5)
print("Your Exam will start with in")
func1(10)

timeout=5

start_time_a=time.time()
start_time.append(start_time_a)
a=input("Question 1: What is the Next Prime Number after 7 =")
q.append(a)
end_time_a=time.time()
end_time.append(end_time_a)

start_time_b=time.time()
start_time.append(start_time_b)
b=input("Question 2: The Product of 131*0*300*4 =")
q.append(b)
end_time_b=time.time()
end_time.append(end_time_b)

start_time_c=time.time()
start_time.append(start_time_c)
c=input("Question 3: List is Muttable(True/False) =")
q.append(c)
end_time_c=time.time()
end_time.append(end_time_c)

start_time_d=time.time()
start_time.append(start_time_d)
d=input("Question 4: tuple is immuttable(True/False) =")
q.append(d)
end_time_d=time.time()
end_time.append(end_time_d)

start_time_e=time.time()
start_time.append(start_time_e)
e=input("Question 5: Solve 23+3÷3=")
q.append(e)
end_time_e=time.time()
end_time.append(end_time_e)

# print(end_time)
# print(start_time)

for i in range(0,5):
    elapsed_time=(end_time[i])-(start_time[i])
    if  elapsed_time > timeout:
        print(f"'Times Up'  limit of {timeout} seconds for Question number {i+1} ,So answer will not consider for valuation")
    else:  
        if q[i]==answer[i]:
            score=score+20
print(f"Your score = {score}")
if score>40:
    print("congratulations you have passed the exam")
else:
    print("Better luck Next time")