import random

# constante
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'engurrupletadora',
    'sofa',
    'dictadura',
    'uribe',
    'pistola',
    'sql'
    'computador',
    'vaso',
    'vaca',
    'ninfomana'
]

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries +=1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('¡Perdiste!')
                print('La palabra correcta era {}'.format(word))
                break

        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter

            letter_indexes = []

            try:
                hidden_word.index('-')
            except ValueError:
                display_board(hidden_word, tries)
                print('')
                print('¡Ganaste!')
                break

def random_word():
    # index = random.randint(0, len(WORDS) - 1)
    # return WORDS[index]
    return random.choice(WORDS)

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * ')

if __name__ == '__main__':
    print('¡Juega al ahorcado!')
    run()