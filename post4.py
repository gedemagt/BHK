# -*- coding: utf-8 -*-
from util import write, watch_video

POSITION = "Sektor 3"

def run(rigtig_bogstav, hackername, hackerpass):
    write("B-HacK har netop oprettet en forbindelse til en sattelit fra {}.".format(POSITION), 0.5, False)
    write("Vi er ret sikre på at de har oprettet en ny server i det område!", 0.5, False)
    write("Vi har et gevaldigt behov for at i skynder jer ned og slukker serveren!", 0.5, False)
    write("I øvrigt...", 0.5, False)
    write("Der sniger sig nogle skumle typer rundt ved mit vindue!", 0.5, False)
    write("Hold lige et øje åbent, for B-HacK's agenter", 0.5, False)
    write("Nå: Skynd jer ned til {}!".format(POSITION), 0.5, False)
    write("Husk lige at der formentligt er bevogtet! De må under inden omstændigheder se jer!", 0.5, False)
    k = write("Er i bevæbnet?")
    if "ja" in k.lower():
        write("Super, i får måske brug for det!", 0.5, False)
    else:
        write("Ærgerligt. Så.. ja, i finder nok ud af det...!", 0.5, False)

    
    write("Ved siden af sluk-knappen er der et bogstav - det skal i have med tilbage!", 0.5, False)
    write("Afsted!")
    
    bogstav = write("Hurtigt - hvad er bogstavet?")
    while bogstav.lower() != rigtig_bogstav.lower():
        bogstav = write("Det er forkert! Prøv igen?")
    write("Super, tak! Vi nærmer os, godt arbejde!", 0.5, False)
    return bogstav

if __name__ == "__main__":    
    run("a")
