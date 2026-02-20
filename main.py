import random
# max=906761326283830153
max=10
print (f"guess a number 1 to {max}")
answer = random.randint(1,max)
guess = 0
while guess != answer:
    guess=int(input())
