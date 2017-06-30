from util import write, watch_video

def run(rigtige_bostav, hackername, hackerpass):
    write('En hackergruppe under navnet Hørebananerne har i lang tid forsøgt at komme ind i Dr. Slims organisations computere for at få et bogstav til koden - men uden held.', 0.5, False)
    write('Hørebananerne har sendt følgende besked til jer:', 0.5, False)
    write('###############', 0.5, False)
    write('@ %s, ', 0.5, False)
    write('Vi kan ikke komme ind i systemet og tiden er ved at løbe ud.', 0.5, False)
    write('Vi har brug for jeres hjælp til at få delen af koden. ', 0.5, False)
    write('Når hacking ikke dur, så må vi prøve andre metoder. ', 0.5, False)
    write('I Dr. Slims organisation er der en ansat ved navn Sonja Behyldebo, som vi tror at vi kan lokke et log ind ud af.', 0.5, False)
    write('Hun er glad for kage - måske I kan overtale hende med det, men HUSK AT I IKKE MÅ AFSLØRE HVEM I ER!', 0.5, False)
    write('Hvis hun opdager at i prøver at snyde jer vil hun ikke hjælpe jer alligevel!', 0.5, False)
    write('Ring til hende på 23804210 og lok brugernavnet og koden ud af hende', 0.5, False)
    write('Tryk ENTER for at forbinde til Dr. Slims computere.')
    write("Forbinder til Dr. Slims computere", 0.5, False)
    write('.', 1, False)
    write('. .', 1, False)
    write('. . .', 1, False)
    write('. . . .', 1, False)
    write('. . . . .', 1, False)
    write('ᶘ ᵒᴥᵒᶅ', 1, False)
    write('Forbundet!', 1, False)
    name = write('Brugernavn: ')
    while name != "AdMiN":
        name = write("Forkert! Prøv igen!")
    
    pw = write('Kodeord: ')
    while pw != "SecretPassWorD":
        pw = write("Forkert! Prøv igen!")
    
    write("Logger ind", 0.5, False)
    write(".", 0.5, False)
    write("..", 0.5, False)
    write("...", 0.5, False)
    write("....", 0.5, False)
    write("Velkommen til Dr. Slims Hemmelig Computer", 0.5, False)
    write("Vores yndlingsbogstav for ugen er {}".format(rigtige_bostav), 0.5, False)
    write("Over and out", 1.5, False)
    write("Forbindelse afsluttet", 0.5, False)
    
if __name__ == "__main__":    
    run("a")
