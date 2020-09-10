import random

guessesTaken = 0

print('Привет,как тебя зовут?')
myName = input()

number = random.randint(1, 20)
print('Что ж, ' + myName + ', я загадываю число от 1 до 20, у тебя есть 6 попыток.')

for guessesTaken in range(6):
    print('Попробуй угадать.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Твое число слишком маленькое.')


    elif guess > number:
            print('Твое число слишком большое.')

    elif guess == number:
            break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Отлчино, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадал число ' + number + '.')
