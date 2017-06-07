# -*- coding: utf-8 -*-

import sys
from app.application import go_for_it_girl

if __name__ == "__main__":
    #try:
    go_for_it_girl(sys.argv[1:])
    #except:
    #    print ("Invalid commmand.")