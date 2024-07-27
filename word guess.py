import random
fruits=['apple','banana','grapes','mango','peach','peer','litchi','watermelon','strawberry','papaya','pomegranate','guava']
animals=['cat','dog','beer','giraffe','deer','peacock','lion','kangaroo','zebra','wolf','sheep','penguin','monkey','cheetah']
stationary=['pen','paper','copy','scale','pencil','inkpot','calculator','stapler','scissors','marker','sharpener','eraser']
score=0
while 1:
    words=fruits+animals+stationary
    random_word=random.choice(words)
    print("WORDS GUESSING GAME")
    if random_word in animals:
        print("Hint:It is an animal.")
    elif random_word in fruits:
        print("Hint:It is a fruit.")

    else:
        print("Hint:It is a stationary.")
    user_guess=''
    chances=5
    while chances>0:
        wrong_guess=0
        for ch in random_word:
            if ch in user_guess:
                print(ch,end=' ')
            else:
                wrong_guess+=1
                print('_',end=' ')
        if wrong_guess==0:
            print('\nCongrats You guess the correct word.The correct word is:',random_word)
            score+=20
            print("Your score is:",score)
            again=input('Do you want to play again?yes or no')
            if again=='yes':
                break
            else:
                quit()
        guess=input('\n Make a guess:')
        user_guess+=guess
        if guess not in random_word:
            chances-=1
            print(f'Wrong.You have {chances} more .')
            if chances==0:
                print('You lost.The correct word is:',random_word)
                print("Your score is:",score)
                restart=input('Do you want to play again?Yes or No:')
                if restart=='n`o':
                    quit()
