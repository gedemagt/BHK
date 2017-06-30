from util import write, watch_video

def run(rigtig_bogstav, hackername, hackerpass):
    write("Er i der?")
    write("Vi har fået skrevet et program der kan aflytte Dr. Slims computere.", 0.5, False)
    write("Problemet er at vi skal installere det ved at placere det direkte på en computer!", 0.5, False)
    write("Vores hacker-ven HaXX0r har overført det til en USB-stik, og givet det til BaHaX.", 0.5, False)
    
    
    write("Men lige inden i smutter:", 0.5, False)
    write("Hvad er blåt og grønt, har otte fingre og tretten tænder?")

    write("Naarh, prøv igen!")
    write("Næh, Kom nu, i ved det godt!")

    write("Nå, nej... Så var der ikke noget alligevel!", 0.5, False)

    write("I kan finde BaHaX nede I sektor 5", 0.5, False)
    write("Han har en b...", 0.5, False)
    write("]@¡  ± ¡} ... }@¡ £{@¡", 0.5, False)
    write("på..@}¡", 0.5, False)
    write("Dårligt signal - forbindelse afbrudt!", 20, False)
    
    write("Fik i overført filerne?! (ja, nej)")
    
    bogstav = ""
    
    if "ja" in k.lower():
        bogstav = write("Super, godt arbejde!")
    else:
        bogstav = write("Elendigt!, Nå, Jeg håber BaHaX gav jer det bogstav han havde på sig alligevel?")
    
    while bogstav.lower() != rigtig_bogstav:
        bogstav = write("Det er forkert! Prøv igen?")
    write("Arh, det ser godt ud!", 0.5, False)
    return bogstav
    
if __name__ == "__main__":    
    run("a")
