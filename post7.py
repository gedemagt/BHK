# -*- coding: utf-8 -*-

from util import write, watch_video

POSITION = "Sektor 5"

def run(rigtige_bogstav, hackername, hackerpass):
    
    write('.', 1, False)
    write('. .', 1, False)
    write('. . .', 1, False)
    write('. . . .', 1, False)
    write('. . . . .', 1, False)
    write('Yez?', 1, False)
    write('Men er der noen?(Tryk ENTER)')
    write('Ahh men er det jer {}?(Tryk ENTER)'.format(hackername))
    write('Godt godt godt... Vi har modtaget en opgave fra hackergruppen Hørebananerne...(Tryk ENTER)')
    write('Gå til {}. Her skal I finde en walkie talkie og bruge den til at komme i kontakt med manden fra hørebananerne(Tryk ENTER)'.format(POSITION))
    write('For at han ved at I er dem i udgiver jer for at være, så skal I fortælle ham, hvad der SKAL være på is på BHK til festen!'.format(POSITION))
    write('Herefter vil han give jer næste ord i rækkens i')
    bogstav = write('Koden fra posten fra B-HacK: ')
    while True:
        if bogstav.lower() == rigtige_bogstav.lower():
            write('Sådan! I klarede den. Gå videre til næste opgave (Tryk ENTER)')
            return
        else:
            bogstav = write('Forkert kode fra posten. Prøv igen')


if __name__ == "__main__":    
    run("a")
