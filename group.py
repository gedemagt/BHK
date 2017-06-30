import intro
from util import write
from collections import OrderedDict

class Group:

    def __init__(self):
        self.posts = OrderedDict()
        
    def add_post_letter(self, post, letter):
        self.posts.update({letter:post.run})
        
    def go(self, start=0):
        print(chr(27) + "[2J")
        k = 0
        if start == 0:
            hackername, hackerpass = intro.run()
        else:
            hackername, hackerpass = ("test","test")
        
        for letter,post in self.posts.items():
            k = k+1
            if k < start:
                continue
            post(letter, hackername, hackerpass)
            write("Tryk (ENTER)")
        
        write("Tak - det var alt")
        write("Afvent instruktioner")
        write("Ti stille!")
        while True:
            write("Afvent!")
            
            
