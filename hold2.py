# -*- coding: utf-8 -*-
import post1, post3, post4, post6, post7
import group
import sys
import util

if "debug" in sys.argv:
    util.DEBUG = True
else:
    util.DEBUG = False


g = group.Group()
g.add_post_letter(post3, "Dr")
g.add_post_letter(post4, "i")
g.add_post_letter(post6, "undertøj")
g.add_post_letter(post7, "dame")
g.add_post_letter(post1, "Slim går")
g.go(0 if len(sys.argv)==1 else int(sys.argv[1]))



