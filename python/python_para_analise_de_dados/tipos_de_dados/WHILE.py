import random

Parar = 0
while Parar <= 55:
    print(Parar)
    Parar += 1

Loop = 0
while Loop <= 10:
    print(Loop)
    if Loop == 5:
        for x in range(10):
            print(random.random())
    Loop += 1

while True:
    Eu = random.randint(0, 10)
    Contra_Voces = random.randint(0, 10)

    print('Eu tirei o valor', Eu)
    print('Vcs tiraram o', Contra_Voces)

    if Eu > Contra_Voces:
        print('Ganhei!!!')
        break
    else:
        print('Voces ganharam!')
        break
    print('\n')

