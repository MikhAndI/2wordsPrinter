from random import choice
from time import sleep

words = ['leg', 'head', 'tummy', 'arm', 'ears', 'eyes']
w_1 = input('First word? ')
w_2 = input('Second word? ')
while True:
    print(w_1)
    print(w_2)
    print(f'My {choice(words)}!')
    sleep(1)
