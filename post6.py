# -*- coding: utf-8 -*-
from util import write, watch_video

POSITION = 'Sektor 4'

def run(rigtige_bostav, hackername, hackerpass):
    write('En hackergruppe under navnet Hørebananerne har i lang tid forsøgt at komme ind i Dr. Slims organisations computere - men uden held.', 0.5, False)
    write('De er tæt på at få brugernavnet og kodeordet, men har brug for jeres hjælp til at skaffe dem endeligt. I skal logge ind på Dr Slims Computer og finde det næste ord i rækken...', 0.5, False)
    write('###############', 0.5, False)
    write('@ %s, ', 0.5, False)
    write('', 0.5, False)
    write('Gå til {} og mød hackeren fra Hørebananerne. Han vil forklare jer hvordan I skaffer brugernavnet og kodeordet.'.format(POSITION), 0.5, False)
    write('Tryk ENTER for at forbinde til Slims computer. Ordet I skal bruge skulle stå så snart i logger ind.', 0.5, True)
    write('Forbinder!', 1, False)
    write('.', 1, False)
    write('. .', 1, False)
    write('. . .', 1, False)
    write('. . . .', 1, False)
    write('. . . . .', 1, False)
    write('ᶘ ᵒᴥᵒᶅ', 1, False)
    write('Forbundet\nVelkommen til Dr. Slims computer!', 1, False)
    name = write('Brugernavn: ')
    while name != "slimowich":
        name = write("Forkert! Prøv igen!")
    
    pw = write('Kodeord: ')
    while pw != "blondeundertøj":
        pw = write("Forkert! Prøv igen!")
    
    write("Logger ind", 0.5, False)
    write(".", 0.5, False)
    write("..", 0.5, False)
    write("...", 0.5, False)
    write("....", 0.5, False)
    write("Velkommen til Dr. Slims Hemmelig Computer", 0.5, False)
    write("Sekretær, det næste ord i rækken er '{}'".format(rigtige_bostav), 0.5, False)
    write("Over and out", 1.5, False)
    write("Forbindelse afsluttet", 0.5, False)
    
if __name__ == "__main__":    
    run("a")
