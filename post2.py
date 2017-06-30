from util import write, watch_video


def run(rigtig_bogstav):
    write("Jeg har netop opsnappet en kode fra wifi-netværket, men jeg forstår den ikke!", 0.5, False)
    write("Jeg håber i kan hjælpe mig! Jeg tror det er en del af kodeordet vi skal bruge!", 0.5, False)
    write("Er i stadig i området?", 0.5, False)
    
    
    if "ja" in k.lower():
        write("Super, så håber jeg i er klar på endnu en opgave!", 0.5, False)
    else:
        write("Ærgerligt.. Men der går vel en bus!", 0.5, False)
    
    
    
    write("Nede ved Sektor 2 er der tit observeret B-HacK folk ", 0.5, False)
    write("Er i der?!?!", 0.5, False)
    write("HALLO!?", 0.5, False)
    write("Godt så!", 0.5, False)
    write("Jeg spiller en video for jer lige om lidt. I skal huske rigtig godt efter hvad der sker i filmen.", 0.5, False)
    write("Bagefter skal i skynde jer ned og prøve at finde det de har gemt!", 0.5, False)
    write("Er i klar til at se videoen? (Tryk ENTER)")

    watch_video()
    k = write("Vil i se videoen igen? (ja, nej)")
    while k.lower() in ["jo","ja","okay"]:
        watch_video()
        k = write("Vil i se videoen igen? (ja, nej)")


    write("Skynd jer nu ned til Sektor 2!", 0.5, False)
    write("Der vil i finde en fra vores gruppe!", 0.5, False)
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
    write("Forbindelse afbrudt!", 20, False)
    
    bogstav = write("Fik i fat i bogstavet? Hvad er det?")
    while bogstav.lower() != rigtig_bogstav:
        bogstav = write("Det er forkert! Prøv igen?")
    write("Det ser rigtigt ud!", 0.5, False)
    return bogstav
