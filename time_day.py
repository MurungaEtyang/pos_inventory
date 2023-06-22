import datetime as dt
from time import *

def day(han):       #find what time of day is it?
    t = han.datetime.now()
    h = t.strftime("%H")
    h = int(h)
    
    if h < 12:
        return "Good morning it's"
        h = 0
        t = 0
    if h < 16:
        return "Good afternoon it's"
        h = 0
        t = 0
    if h < 19:
        return "Good evening it's"
        h = 0
        t = 0
    if h < 24:
        return "Good night it's"
        h = 0
        t = 0
    return "midnight it's"
    h = 0
    t = 0
    
a = day(dt)

