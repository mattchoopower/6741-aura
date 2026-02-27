import random
max = 100
print(f"guess a number 1 to {max}")
answer = random.randint(1,max)
guess = 0
while guess != answer:
    guess = input()
    try:
        guess=int(guess)
    except:
        print("not a NUMBER go back to ur mommy")
        continue
    if guess == answer:
        print("thats correct, nice job!")
    if guess < answer:
        print("too low, even slef is better than u!")
    if guess > answer:
        print("TOO HIGH!")
