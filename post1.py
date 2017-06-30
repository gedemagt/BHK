from util import write, watch_video

def run(rigtig_bogstav, hackername, hackerpass):
    write("Vores venner i Dark Army har netop sendt et videoklip, de sagde vi skal se!", 0.5, False)
    write("Det kommer fra en lagerbygning vi ved der bliver brugt af B-HacK!", 0.5, False)
    write("Vi har en mistanke om at B-HacK gemmer endnu en vigtig ledetråd dernede!", 0.5, False)
    write("Hallo?!", 0.5, False)
    write("Er i der?!?!", 0.5, False)
    write("HALLO!?", 0.5, False)
    write("Godt så!", 0.5, False)
    write("Skynd jer nu ned til Sektor 2!", 0.5, False)
    write("Der vil i finde en fra vores gruppe!", 0.5, False)
    write("Han spiller en video for jer. I skal huske rigtig godt efter hvad der sker i filmen.", 0.5, False)
    write("Bagefter skal i skynde jer ind i et rum og prøve at finde det B-HacK har gemt!", 0.5, False)
    #write("Er i klar til at se videoen? (Tryk ENTER)")

    #watch_video()
    #k = write("Vil i se videoen igen? (ja, nej)")
    #while k.lower() in ["jo","ja","okay"]:
    #    watch_video()
    #    k = write("Vil i se videoen igen? (ja, nej)")


    k =write("Nogle spørgsmål? (ja, nej)")

    if "ja" in k.lower():
        write("Det er der desværre ikke tid til. Afsted!!!", 0.5, False)
    else:
        write("Super. Afsted!!!", 0.5, False)

    write("Jeg afbryder forbindelsen et øjeblik!", 0.5, False)
    write(".", 0.5, False)
    write("..", 0.5, False)
    write("...", 0.5, False)
    write("....", 0.5, False)
    write("Forbindelse afbrudt!", 1, False)
    write("", 1, False)
    write("", 1, False)
    write("", 1, False)
    write("", 1, False)
    write("", 1, False)
    
    bogstav = write("Skriv bogstavet til mig, så snart i har fået det!")
    while bogstav.lower() != rigtig_bogstav:
        bogstav = write("Det er forkert! Prøv igen?")
    write("Det ser rigtigt ud!", 0.5, False)
    return bogstav
    
if __name__ == "__main__":    
    run("a")
