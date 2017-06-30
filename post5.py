import time
from util import write, watch_video

def run():
    
    write('Yez?', 0.5, False)
    write('Men er der noen?(Tryk ENTER)')
    write('Ahh men er det jer {0}?')
    write('Godt godt godt... Vi har modtaget en opgave fra Dark Army...(Tryk ENTER)')
    write('Gå til post 3. Her vil I møde én af vores venner fra Dark Army, som vil forklare jer, hvad I skal gøre.(Tryk ENTER)')
    write('I får et svar fra posten, som vi skal bruge til at knække Dr. Slims B-HacK. (Tryk ENTER)')


    bogstav = write('Fra posten: ')
    while True:
        
        if bogstav == 'D' or bogstav == 'd' or bogstav == 'sonja':

            write('Sådan! I klarede den. Gå videre til næste opgave (Tryk ENTER)')
            write('Forbindelse afbrudt ....')
            return
        else:
            bogstav = write('Forkert. Prøv igen')

run()
