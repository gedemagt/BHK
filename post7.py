from util import write, watch_video


def run(rigtige_bogstav, hackername, hackerpass):
    
    write('.', 1, False)
    write('. .', 1, False)
    write('. . .', 1, False)
    write('. . . .', 1, False)
    write('. . . . .', 1, False)
    write('Yez?', 1, False)
    write('Men er der noen?(Tryk ENTER)')
    write('Ahh men er det jer {0}?(Tryk ENTER)')
    write('Godt godt godt... Vi har modtaget en opgave fra Dark Army...(Tryk ENTER)')
    write('Gå til post 3. Her vil I møde én af vores venner fra Dark Army, som vil forklare jer, hvad I skal gøre.(Tryk ENTER)')
    write('Husk koden og find walkie talkien ved post 2(Tryk ENTER)')
    write('En af Dr Slims folk fra B-HacK har en walkie talkie. I skal udgive jer for at være fra B-HacK.(Tryk ENTER)')
    write('Giv ham kodeordet fra post 1 og lok ham til at give jer et koden fra posten:')

    bogstav = write('Koden fra posten fra B-HacK: ')
    while True:
        if bogstav == rigtige_bogstav:

            write('Sådan! I klarede den. Gå videre til næste opgave (Tryk ENTER)')
            return
        else:
            bogstav = write('Forkert kode fra posten. Prøv igen')


if __name__ == "__main__":    
    run("a")
