import random, time
min_val, max_val = 1, 6
roll_again = True
while roll_again:
    print('Rolling the dices', end='', flush=True)
    
    # Add a delay between dots to create an animation
    for _ in range(random.randint(4, 7)):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print('\nThe values are: ')
    print(random.randint(min_val, max_val), random.randint(min_val, max_val))

    roll_again = True if input('Roll the dices Again? (Y/N) ').lower() == 'y' else False
