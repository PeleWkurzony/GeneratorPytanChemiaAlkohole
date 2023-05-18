import random


def read_lines(path: str) -> int:
    return len(open(path).readlines())


def get_question() -> str:
    question = random.randint(0, 1)
    if question == 0:
        # alkohole
        with open('alkohole.txt', 'r') as alkohole_txt, open('alkoholePytania.txt', 'r') as pytania_txt:
            nr_pytania = random.randint(0, alkohole_pytania - 1)
            nr_alkoholu = random.randint(0, alkohole - 1)
            pytanie = ''
            c = 0
            while c != nr_pytania - 1:
                pytania_txt.readline()
                c += 1
            pytanie = pytania_txt.readline()

            c = 0

            while c != nr_alkoholu - 1:
                alkohole_txt.readline()
                c += 1
            alkohol = alkohole_txt.readline()

            pytania_txt.close()
            alkohole_txt.close()

            return pytanie.format(alkohol)
    else:
        # fenole
        with open('fenole.txt', 'r') as fenole_txt, open('fenolePytania.txt', 'r') as pytania_txt:
            nr_pytania = random.randint(0, fenole_pytania - 1)
            nr_fenolu = random.randint(0, fenole - 1)
            pytanie = ''
            c = 0
            while c != nr_pytania - 1:
                pytania_txt.readline()
                c += 1
            pytanie = pytania_txt.readline()

            c = 0

            while c != nr_fenolu - 1:
                fenole_txt.readline()
                c += 1
            fenol = fenole_txt.readline()

            fenole_txt.close()
            pytania_txt.close()

            return pytanie.format(fenol)


alkohole = read_lines('alkohole.txt')
alkohole_pytania = read_lines('alkoholePytania.txt')
fenole = read_lines('fenole.txt')
fenole_pytania = read_lines('fenolePytania.txt')

while True:
    print(get_question())
    print('-------')
