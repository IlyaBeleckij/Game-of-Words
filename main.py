import time
import random
import os
kill = False
while True:
    if kill:
        break
    os.system('cls')
    score = 0
    print("HALO\n")
    print("Чем больше слов запомните - тем лучше")
    nick = input('Nickname: ')
    for i in range(10):
        os.system('cls')
        print('  Loading:')
        print('#' * i)
        time.sleep(0.1)
    lib = open('BIN.txt', encoding='utf-8')
    slovar = lib.readlines()
    for i in range(len(slovar)):
        slovar[i] = slovar[i][:-1]
    for i in range(10):
        os.system('cls')
        now = random.sample(slovar, i + 2)
        for j in now:
            print(j, end=" ")
        print()
        time.sleep(2 + 0.6 * i)
        os.system('cls')
        print('Введите слова:')
        u_words = input().split(' ')
        if set(u_words) != set(now):
            print('Ваш счет:', score)
            print('Сыграть еще раз? Д/Н')
            if input() == 'Н':
                kill = True
            break
        score += i + 2
