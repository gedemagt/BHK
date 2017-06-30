import intro

class Group:

    def __init__(self):
        self.posts = dict()
        
    def add_post_letter(self, post, letter):
        self.posts.update({letter:post.run})
        
    def go(self):
        hackername, hackerpass = intro.run()
        for letter,post in self.posts.items():
            post(letter, hackername, hackerpass)
            
