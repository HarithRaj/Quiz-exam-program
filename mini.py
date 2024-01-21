import time

q=[]
end_time=[]
score=0
answer=["a","d","b","c","c"]

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

print("INSTRUCTIONS")
print("READ INSTRUCTIONS CAREFULLY")
print("1. TOTAL 5 QUESTIONS.")
print("2. YOU HAVE TOTAL 25 SECONDS FOR ALL QUESTIONS.")
print("3. IF YOU TAKE MORE THAN 25 SECONDS,THE ANSWERS AFTER 25 SECONDS WILL NOT BE CONSIDERED FOR VALUATION.")
input('Press ENTER KEY to START EXAM')

print("Your Exam will start with in")
func1(10)

timeout=25

start_time=time.time()

a=input("Question 1: What is the Next Prime Number after 7 \na) 11\t\tb) 13\nc) 15\t\td) 19\nAnswer=")
q.append(a)
end_time_a=time.time()
end_time.append(end_time_a)

b=input("Question 2: The Product of 131*0*300*4 \na) 1\t\tb) 131\nc) 10\t\td) 0\nAnswer=")
q.append(b)
end_time_b=time.time()
end_time.append(end_time_b)

c=input("If we minus 712 from 1500, how much do we get? \na) 778\t\tb) 788\nc) 768\t\td) 758\nAnswer=")
q.append(c)
end_time_c=time.time()
end_time.append(end_time_c)

d=input("Find the missing terms in multiple of 3: 3, 6, 9, __, 15 \na) 10\t\tb) 11\nc) 12\t\td) 13\nAnswer=")
q.append(d)
end_time_d=time.time()
end_time.append(end_time_d)

e=input("Question 5: Solve 23+3÷3= \na) 0\t\tb) 27/3\nc) 24\t\td) 13\nAnswer=")
q.append(e)
end_time_e=time.time()
end_time.append(end_time_e)

# print(end_time)
# print(start_time)

for i in range(0,5):
    elapsed_time=(end_time[i])-(start_time)
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
