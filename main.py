import random
animals = ['snik','fish','shark','trutal']
chosen_animal = random.choice(animals)
display_animal = ['-' for _ in chosen_animal ]
attempts = 4
while attempts > 0 and '-' in display_animal:
    print('\n' + ' '.join(display_animal))
    guess = input('Guess letter of animal name: ')
    if guess in chosen_animal:
        for x,y in enumerate(chosen_animal):
            if y == guess:
                display_animal[x]=guess
    else:
        attempts -= 1
        print('you chance is over,try later!!')
if '-' not in display_animal:
    print('gongrats you won the word was ' .join(display_animal))
else:
    print('sorry you lost the word was ' + chosen_animal)    
