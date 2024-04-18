score=0
print("Question 1:what is the capital of france?")
answer1=input("a) paris\n b)rome\n c) madrid\nyour answer:")
if answer1=='a':
    score+=1

print("Question 1:which fruit has the highest oil content?")
answer2 = input("a) avacado\n b) tomato\n c) pumpkin\nyour answer:")
if answer2== 'a':
    score += 1

print("Question 1:where was the kiwi fruit first grown?")
answer3 = input("a) china\n b) usa\n c) uk\nyour answer:")
if answer3== 'a':
    score += 1

print("quiz completed!")
print("you got score out of 3 questions correct.",score)
