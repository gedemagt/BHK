import time
import random
import sys

TAG = ">>"
DEBUG = True

def write(message, delay=0, inp=True):

    sys.stdout.write("{} ".format(TAG))
    sys.stdout.flush()
        
    for k in message:
        v = random.uniform(0.01, 0.1) if not DEBUG else 0
        sys.stdout.write(k)
        sys.stdout.flush()
        time.sleep(v)
    
    if inp:
        temp = input("\n>> ")
        return temp
    else:
        sys.stdout.write("\n")
        time.sleep(delay)
    
def watch_video():
    pass
    
    
def warmupTal():
    randtal = random.randint(1,100)
    write(randtal, 0, False)
    counter = 5
    while counter > 0:

        while True:
            guess = write('Gæt tallet mellem 1 - 100. I har %s forsøg tilbage' % counter)
            if guess == 'N':
                return 0
            try:
                guess = int(guess)
                break
            except:
                write('Gæt skal være et tal eller bogstavet "N" for at afbryde opgaven.\n')

        if guess == randtal:
            write('I gættede rigtigt. Tallet var %s. Notér dette - det skal bruges i kodeordet.\n'%randtal)
            return 1
        elif guess < randtal:
            write('Forkert tal. Prøv igen. Det rigtige tal er højere end jeres gæt.')
        else:
            write('Forkert tal. Prøv igen. Det rigtige tal er lavere end jeres gæt.')
        counter -= 1
