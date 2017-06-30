import post1, post3, post4, post6, post7
import group
import sys


g = group.Group()
g.add_post_letter(post1, "S")
g.add_post_letter(post3, "G")
g.add_post_letter(post4, "D")
g.add_post_letter(post6, "U")
g.add_post_letter(post7, "R")
g.go(0 if len(sys.argv)==1 else int(sys.argv[1]))


