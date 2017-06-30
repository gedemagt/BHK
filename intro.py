from util import write, watch_video
import time

def run():
    write('Velkommen til B-HacK', 0.5, False)
    write('B-HacK er et program som kan hjælpe med at knække koden og stoppe Dr. Slims onde plan.', 0.5, False)
    write('For at være sikre på at I er anonyme for Dr. Slim, er det vigtigt at I vælger et hackernavn og kode, som I skal bruge ved opgaver.', 0.5, False)

    hackername = write('Skriv jeres gruppes hackernavn: ')
    hackerpass = write('Velkommen %s. Vælg et kodeord: '% hackername)
    write('Undersøger hvor I sidder for at kunne gøre jer usynlige på internettet', 0.5, False)
    write('.', 1, False)
    write('. .', 1, False)
    write('. . .', 1, False)
    write('. . . .', 1, False)
    write('. . . . .', 1, False)
    write('ᶘ ᵒᴥᵒᶅ\n', 1, False)
    #input('Klar! Tryk ENTER for at starte')
    #webbrowser.get('https://www.google.dk/maps/place/Frijsenborg+Efterskole/@56.245319,9.855664,640m/data=!3m1!1e3!4m5!3m4!1s0x464c0c3050549829:0xba8479c42ecb6127!8m2!3d56.245319!4d9.857858', using="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

    return hackername, hackerpass
    
if __name__ == "__main__":    
    run()
